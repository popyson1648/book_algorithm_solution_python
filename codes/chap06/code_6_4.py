"""lower_boundの活用：ペア和

対応: 6.6
計算量: 時間 O(N log N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap06/code_6_4.cpp
"""

import sys
from bisect import bisect_left
from math import inf


def minimum_pair_sum(a, b, k):
    b = sorted(b)
    result = inf
    for x in a:
        # 一方の値xを固定し、和がk以上になる相手の最小値を探す。
        index = bisect_left(b, k - x)
        # k - x 以上の要素がなければ、index は len(b) になる。
        if index < len(b):
            result = min(result, x + b[index])
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, k = next(it), next(it)
    a = [next(it) for _ in range(n)]
    b = [next(it) for _ in range(n)]
    print(minimum_pair_sum(a, b, k))


if __name__ == "__main__":
    main()
