"""Frogのメモ化再帰

対応: 5.3
計算量: 時間 O(N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap05/code_5_6.cpp
"""

import sys
from math import inf


def frog(h):
    dp = [inf] * len(h)

    def rec(i):
        # この足場までの最小コストが計算済みなら再利用する。
        if dp[i] < inf:
            return dp[i]
        # 最初の足場には、移動せずコスト0で到達できる。
        if i == 0:
            return 0
        # 1つ前と2つ前の足場から来る場合を比べる。
        res = rec(i - 1) + abs(h[i] - h[i - 1])
        if i > 1:
            res = min(res, rec(i - 2) + abs(h[i] - h[i - 2]))
        dp[i] = res
        return res

    return rec(len(h) - 1)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    print(frog([next(it) for _ in range(n)]))


if __name__ == "__main__":
    main()
