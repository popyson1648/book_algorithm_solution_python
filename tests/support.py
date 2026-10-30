"""翻訳の索引、モジュール読み込み、検証対象の記録。外部依存なし。"""
import contextlib
import importlib.util
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'docs/catalog.json').read_text())
BY_KEY = {item['key']: item for item in CATALOG}
VISITED = set()
CHECKS = {}
CURRENT_TEST = 'direct'


def mark(key):
    VISITED.add(key)
    CHECKS.setdefault(key, set()).add(CURRENT_TEST)


def load(key):
    mark(key)
    path = ROOT / BY_KEY[key]['path']
    name = 'translation_' + key.replace('/', '_')
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def capture(function, *args):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        result = function(*args)
    return result, output.getvalue()


def run_main(key, data=''):
    module = load(key)
    old_stdin = sys.stdin
    stream = io.TextIOWrapper(io.BytesIO(data.encode()), encoding='utf-8')
    try:
        sys.stdin = stream
        return capture(module.main)[1]
    finally:
        sys.stdin = old_stdin
        stream.close()
