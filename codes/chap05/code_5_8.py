"""編集距離

対応: 5.5
計算量: 時間・領域 O((|S|+1)(|T|+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap05/code_5_8.cpp
"""

import sys
from math import inf


def edit_distance(s, t):
    # dp[i][j] はsの先頭i文字をtの先頭j文字に変える最小操作回数。
    dp = [[inf] * (len(t) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = 0
    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            # 末尾の文字が同じなら操作不要、異なれば1回の変更が必要。
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + (s[i - 1] != t[j - 1]))
            if i > 0:  # 削除
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:  # 挿入
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    return dp[-1][-1]


def main():
    s, t = sys.stdin.read().split()
    print(edit_distance(s, t))


if __name__ == "__main__":
    main()
