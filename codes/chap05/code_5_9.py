"""区間分割の最小コスト

対応: 5.6
計算量: 時間 O(N²)、DP領域 O(N)、入力領域 O(N²)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap05/code_5_9.cpp
"""

import sys
from math import inf


def partition_cost(c):
    n = len(c) - 1
    # dp[i] は位置iまでを分割するときの最小コスト。
    dp = [inf] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        # 最後の区間を [j, i) とし、それより前の最小コストに加える。
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + c[j][i])
    return dp[n]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    c = [[next(it) for _ in range(n + 1)] for _ in range(n + 1)]
    print(partition_cost(c))


if __name__ == "__main__":
    main()
