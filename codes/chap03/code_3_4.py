"""K以上となるペア和の最小値

対応: 3.4
計算量: 時間 O(N²)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap03/code_3_4.cpp
"""

import sys
from math import inf


def minimum_pair_sum(a, b, k):
    result = inf
    for x in a:
        for y in b:
            if x + y < k:
                continue
            if x + y < result:
                result = x + y
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, k = next(it), next(it)
    a = [next(it) for _ in range(n)]
    b = [next(it) for _ in range(n)]
    print(minimum_pair_sum(a, b, k))


if __name__ == "__main__":
    main()
