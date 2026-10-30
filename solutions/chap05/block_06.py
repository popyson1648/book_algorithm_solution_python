"""K個以内の部分和：個数をDP値にする

対応: 章末問題5.4
計算量: 時間・領域 O(N(W+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys
from math import inf


def subset_sum_at_most_k(a, target, limit):
    # dp[i][j] は先頭i個で和jを作る最小個数。作れない場合は無限大。
    dp = [[inf] * (target + 1) for _ in range(len(a) + 1)]
    dp[0][0] = 0
    for i in range(len(a)):
        for j in range(target + 1):
            # この要素を選ばない場合は、必要個数を引き継ぐ。
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            # この要素を選ぶ場合は、残りの和を作る必要個数に1を加える。
            if j >= a[i]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - a[i]] + 1)
    return dp[-1][target] <= limit


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, limit, target = next(it), next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if subset_sum_at_most_k(a, target, limit) else "No")


if __name__ == "__main__":
    main()
