"""最大差

対応: 章末問題3.4
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

import sys
from math import inf


def spread(a):
    smallest, largest = inf, -inf
    for value in a:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return largest - smallest


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    print(spread(a))


if __name__ == "__main__":
    main()
