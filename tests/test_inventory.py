"""固定した原文・翻訳・出典一覧の完全性と構文を検証する。"""
import ast
import hashlib
import json
from pathlib import Path
import unittest

from support import BY_KEY, CATALOG, ROOT


class InventoryTests(unittest.TestCase):
    def test_one_to_one_inventory(self):
        refs = json.loads((ROOT / 'tests/reference/manifest.json').read_text())
        self.assertEqual(len(CATALOG), 111)
        self.assertEqual(len(BY_KEY), 111)
        self.assertEqual(sum(x['key'].startswith('codes/') for x in CATALOG), 67)
        self.assertEqual(len(refs), 111)
        expected_paths = {x['path'] for x in CATALOG}
        actual_paths = {str(p.relative_to(ROOT)) for folder in ('codes', 'solutions')
                        for p in (ROOT / folder).rglob('*.py')}
        self.assertEqual(expected_paths, actual_paths)
        keys = set()
        for ref in refs:
            path = Path(ref['reference'])
            kind = path.parts[2]
            chapter = int(path.parts[3][4:])
            number = int(ref['block']) if kind == 'solutions' else int(path.stem.split('_')[-1])
            key = f'{kind}/{chapter}/{number}'
            keys.add(key)
            text = (ROOT / path).read_text()
            original_bytes = text.encode(ref.get('encoding', 'utf-8'))
            self.assertEqual(hashlib.sha256(original_bytes).hexdigest(), ref['sha256'])
            self.assertEqual(BY_KEY[key]['source'], ref['source'])
        self.assertEqual(keys, set(BY_KEY))

    def test_syntax_and_provenance(self):
        for item in CATALOG:
            with self.subTest(path=item['path']):
                text = (ROOT / item['path']).read_text()
                tree = ast.parse(text, filename=item['path'])
                doc = ast.get_docstring(tree)
                self.assertIn(item['commit'], doc)
                self.assertIn(item['section'], doc)
                self.assertIn(item['complexity'], doc)
