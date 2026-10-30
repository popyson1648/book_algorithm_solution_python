"""全検証を実行する。例: python3 -B tests/run_checks.py --report docs/verification.json"""
import argparse
import json
import platform
import subprocess
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
import support
from support import BY_KEY, CHECKS, ROOT, VISITED


class TrackingResult(unittest.TextTestResult):
    def startTest(self, test):
        support.CURRENT_TEST = test.id()
        super().startTest(test)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', type=Path, help='成功時のみ検証結果JSONを保存する')
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.discover(str(ROOT / 'tests'))
    result = unittest.TextTestRunner(verbosity=2, resultclass=TrackingResult).run(suite)
    missing = sorted(set(BY_KEY) - VISITED)
    if not result.wasSuccessful() or missing:
        if missing:
            print('動作確認されなかった翻訳:', missing, file=sys.stderr)
        return 1
    from test_differential import COMPARISONS, DifferentialTests
    report = {
        'upstream_commit': next(iter(BY_KEY.values()))['commit'],
        'python': platform.python_version(),
        'platform': platform.platform(),
        'compiler_command': DifferentialTests.compiler,
        'compiler_version': subprocess.check_output(DifferentialTests.compiler + ['--version'], text=True).splitlines()[0],
        'test_methods': result.testsRun,
        'translated_units': len(BY_KEY),
        'behavior_checked_units': len(VISITED),
        'cpp_cli_comparisons': COMPARISONS,
        'result': 'passed',
        'units': [{'key': key, 'path': BY_KEY[key]['path'],
                   'behavior': 'passed', 'syntax': 'passed', 'checks': sorted(CHECKS[key])} for key in sorted(VISITED)],
    }
    print(f'検証成功: {len(VISITED)}/{len(BY_KEY)}件、C++ CLI比較 {COMPARISONS}ケース')
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
