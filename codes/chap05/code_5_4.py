"""Frogの配る遷移

対応: 5.2–5.3
計算量: 時間 O(N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap05/code_5_4.cpp
"""

import sys
from math import inf


def frog(h):
    n = len(h)
    # dp[i] は足場iまでの最小コスト。まだ求めていない値は無限大にする。
    dp = [inf] * n
    # 最初の足場には、移動せずコスト0で到達できる。
    dp[0] = 0
    # 移動元の最小コストを使い、次の足場と2つ先の足場を更新する。
    for i in range(n):
        if i + 1 < n:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i] - h[i + 1]))
        if i + 2 < n:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i] - h[i + 2]))
    return dp[-1]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    print(frog([next(it) for _ in range(n)]))


if __name__ == "__main__":
    main()
