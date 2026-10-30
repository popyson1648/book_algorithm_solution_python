"""線形探索による最小値

対応: 3.3
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap03/code_3_3.cpp
"""

import sys
from math import inf


def minimum(a):
    result = inf
    for value in a:
        if value < result:
            result = value
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    print(minimum([next(it) for _ in range(n)]))


if __name__ == "__main__":
    main()
