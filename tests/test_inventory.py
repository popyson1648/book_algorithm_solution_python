"""固定した原文・翻訳・出典一覧の完全性と構文を検証する。"""
import ast
import hashlib
import json
import unittest

from support import BY_KEY, CATALOG, ROOT, REFERENCE_MANIFEST, REFERENCES, reference_text


class InventoryTests(unittest.TestCase):
    def test_one_to_one_inventory(self):
        refs = REFERENCE_MANIFEST
        self.assertEqual(len(CATALOG), 111)
        self.assertEqual(len(BY_KEY), 111)
        self.assertEqual(sum(x['key'].startswith('codes/') for x in CATALOG), 67)
        self.assertEqual(len(refs), 111)
        self.assertEqual(len(REFERENCES), 111)
        expected_paths = {x['path'] for x in CATALOG}
        actual_paths = {str(p.relative_to(ROOT)) for folder in ('codes', 'solutions')
                        for p in (ROOT / folder).rglob('*.py')}
        self.assertEqual(expected_paths, actual_paths)
        keys = set()
        for ref in refs:
            key = ref['key']
            keys.add(key)
            self.assertEqual(ref['reference'], 'references/' + ref['source'])
            text = reference_text(key)
            original_bytes = text.encode(ref.get('encoding', 'utf-8'))
            self.assertEqual(hashlib.sha256(original_bytes).hexdigest(), ref['sha256'])
            self.assertEqual(BY_KEY[key]['source'], ref['source'])
        self.assertEqual(keys, set(BY_KEY))

    def test_upstream_snapshot(self):
        snapshot = json.loads((ROOT / 'docs/upstream_snapshot.json').read_text())
        self.assertEqual({item['commit'] for item in CATALOG}, {snapshot['commit']})
        self.assertEqual(len(snapshot['files']), 85)
        expected = {item['path'] for item in snapshot['files']}
        actual = {p.relative_to(ROOT / 'references').as_posix()
                  for p in (ROOT / 'references').rglob('*') if p.is_file()}
        self.assertEqual(actual, expected)
        for item in snapshot['files']:
            with self.subTest(path=item['path']):
                data = (ROOT / 'references' / item['path']).read_bytes()
                blob = b'blob ' + str(len(data)).encode() + b'\0' + data
                self.assertEqual(hashlib.sha1(blob).hexdigest(), item['git_blob'])

    def test_syntax_and_provenance(self):
        for item in CATALOG:
            with self.subTest(path=item['path']):
                text = (ROOT / item['path']).read_text()
                tree = ast.parse(text, filename=item['path'])
                doc = ast.get_docstring(tree)
                self.assertIn(item['commit'], doc)
                self.assertIn(item['section'], doc)
                self.assertIn(item['complexity'], doc)
