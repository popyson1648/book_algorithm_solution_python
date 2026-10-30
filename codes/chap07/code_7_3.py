"""Multiple Array：後ろから条件を満たす

対応: 7.4
計算量: 時間 O(N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap07/code_7_3.cpp
"""

import sys


def multiple_array(pairs):
    total = 0
    for a, b in reversed(pairs):
        # 後ろの要素で行った操作は、この要素にも加算されている。
        a += total
        remainder = a % b
        delta = 0 if remainder == 0 else b - remainder
        total += delta
    return total


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    print(multiple_array([(next(it), next(it)) for _ in range(n)]))


if __name__ == "__main__":
    main()
