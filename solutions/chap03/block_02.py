"""2番目に小さな値

対応: 章末問題3.3
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

import sys
from math import inf


def second_smallest(a):
    first = second = inf
    for value in a:
        if value < first:
            second, first = first, value
        elif value < second:
            second = value
    # 同値も別要素として数える。2要素以上が前提。
    return second


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    print(second_smallest(a))


if __name__ == "__main__":
    main()
