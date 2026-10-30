"""Vacation：前日の状態を持つDP

対応: 章末問題5.1
計算量: 時間 O(N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys


def vacation(a):
    # 幸福度は非負を前提とする。
    dp = [[0] * 3 for _ in range(len(a) + 1)]
    for i in range(len(a)):
        for j in range(3):
            for k in range(3):
                # 前日と同じ活動は選べない。jが前日、kが当日の活動を表す。
                if j == k:
                    continue
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + a[i][k])
    return max(dp[-1])


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [[next(it) for _ in range(3)] for _ in range(n)]
    print(vacation(a))


if __name__ == "__main__":
    main()
