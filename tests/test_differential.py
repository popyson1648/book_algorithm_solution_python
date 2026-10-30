"""89本の実行可能な原文をC++17でコンパイルし、Python CLIと比較する。"""
import concurrent.futures
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

from support import BY_KEY, ROOT, mark, reference_text

CASES = json.loads((ROOT / 'tests/cases.json').read_text())
COMPARISONS = 0


class DifferentialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = os.environ.get('CXX') or shutil.which('clang++') or shutil.which('g++')
        if not compiler:
            raise RuntimeError('C++比較にはclang++またはg++が必要です。CXXでも指定できます。')
        cls.compiler = shlex.split(compiler)
        cls.temp = tempfile.TemporaryDirectory(prefix='book-python-cpp-')
        cls.addClassCleanup(cls.temp.cleanup)
        cls.binaries = {}

        def compile_one(key):
            binary = Path(cls.temp.name) / key.replace('/', '_')
            # 原本を変更せず、一時領域にUTF-8のコンパイル用ソースを作る。
            source = binary.with_suffix('.cpp')
            source.write_text(reference_text(key), encoding='utf-8')
            # アルゴリズム本文は無変更。明示的な標準ヘッダーの補完だけを行う。
            command = cls.compiler + ['-std=c++17', '-O1', '-include', 'algorithm',
                                      '-include', 'cmath', str(source), '-o', str(binary)]
            result = subprocess.run(command, capture_output=True, text=True, timeout=60)
            if result.returncode:
                raise AssertionError(f'{key}: C++コンパイル失敗\n{result.stderr}')
            return key, binary

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            for key, binary in executor.map(compile_one, CASES):
                cls.binaries[key] = binary

    def test_all_executable_translations(self):
        global COMPARISONS
        self.assertEqual(set(CASES), {k for k, v in BY_KEY.items() if v['executable']})
        for key, inputs in CASES.items():
            for index, data in enumerate(inputs):
                with self.subTest(key=key, case=index):
                    cpp = subprocess.run([str(self.binaries[key])], input=data, capture_output=True,
                                         text=True, timeout=10)
                    py = subprocess.run([sys.executable, '-B', str(ROOT / BY_KEY[key]['path'])],
                                        input=data, capture_output=True, text=True, timeout=10)
                    self.assertEqual(cpp.returncode, 0, cpp.stderr)
                    self.assertEqual(py.returncode, 0, py.stderr)
                    self.assertEqual(py.stdout, cpp.stdout)
                    COMPARISONS += 1
                    mark(key)
