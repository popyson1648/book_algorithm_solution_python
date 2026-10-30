"""最長共通部分列の長さ

対応: 章末問題5.7
計算量: 時間・領域 O((N+1)(M+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys


def lcs_length(s, t):
    # dp[i][j] はsの先頭i文字とtの先頭j文字の最長共通部分列の長さ。
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            # 末尾の文字が一致するなら、両方を1文字ずつ伸ばして長さを1増やせる。
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (s[i - 1] == t[j - 1]))
            # sの末尾を使わない場合。
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            # tの末尾を使わない場合。
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[-1][-1]


def main():
    s, t = sys.stdin.read().split()
    print(lcs_length(s, t))


if __name__ == "__main__":
    main()
