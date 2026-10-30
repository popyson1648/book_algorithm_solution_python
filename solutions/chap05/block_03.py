"""0/1部分和のDP

対応: 章末問題5.2
計算量: 時間・領域 O(N(W+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys


def subset_sum(a, target):
    # dp[i][j] は先頭i個の要素で和jを作れるかを表す。
    dp = [[False] * (target + 1) for _ in range(len(a) + 1)]
    dp[0][0] = True
    for i in range(len(a)):
        for j in range(target + 1):
            # この要素を選ばない場合。
            if dp[i][j]:
                dp[i + 1][j] = True
            # この要素を選ぶ場合は、残りの和をそれ以前の要素で作る。
            if j >= a[i] and dp[i][j - a[i]]:
                dp[i + 1][j] = True
    return dp[-1][target]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, target = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if subset_sum(a, target) else "No")


if __name__ == "__main__":
    main()
