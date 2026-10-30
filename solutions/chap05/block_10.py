"""個数制限付き部分和

対応: 章末問題5.6
計算量: 時間・領域 O(N(W+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys
from math import inf


def bounded_subset_sum(items, target):
    # dp[i+1][j] は和jを作るときの品物iの最小使用個数。作れなければ無限大。
    dp = [[inf] * (target + 1) for _ in range(len(items) + 1)]
    dp[0][0] = 0
    for i, (value, limit) in enumerate(items):
        for j in range(target + 1):
            # 以前の品物だけで和jを作れるなら、この品物は0個でよい。
            if dp[i][j] < inf:
                dp[i + 1][j] = 0
            # 個数制限に達していなければ、この品物をもう1個使える。
            if j >= value and dp[i + 1][j - value] < limit:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - value] + 1)
    return dp[-1][target] < inf


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, target = next(it), next(it)
    items = [(next(it), next(it)) for _ in range(n)]
    print("Yes" if bounded_subset_sum(items, target) else "No")


if __name__ == "__main__":
    main()
