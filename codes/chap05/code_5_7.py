"""0/1ナップサック

対応: 5.4
計算量: 時間 O(NW)、領域 O(NW)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap05/code_5_7.cpp
"""

import sys


def knapsack(items, capacity):
    # dp[i][w] は先頭i個の品物から、重さw以下で選べる価値の最大値。
    dp = [[0] * (capacity + 1) for _ in range(len(items) + 1)]
    for i, (weight, value) in enumerate(items):
        for w in range(capacity + 1):
            # この品物を選ぶ場合。
            if w >= weight:
                dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - weight] + value)
            # この品物を選ばない場合。
            dp[i + 1][w] = max(dp[i + 1][w], dp[i][w])
    return dp[-1][capacity]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, capacity = next(it), next(it)
    items = [(next(it), next(it)) for _ in range(n)]
    print(knapsack(items, capacity))


if __name__ == "__main__":
    main()
