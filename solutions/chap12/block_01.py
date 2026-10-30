"""ソート後の各要素の順位

対応: 章末問題12.1
計算量: 時間 O(N log N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap12.md
"""

import sys
from bisect import bisect_left


def coordinate_ranks(a):
    b = sorted(a)
    return [bisect_left(b, value) for value in a]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    for rank in coordinate_ranks(a):
        print(rank)


if __name__ == "__main__":
    main()
