"""同一品物を一度だけ使う遷移

対応: 章末問題5.5・比較用コード片
計算量: 1セルの更新 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

def transition(dp, a, i, j):
    dp[i + 1][j] |= dp[i][j]
    if j >= a[i]:
        # 前の行を参照するため、この要素を使えるのは1回だけ。
        dp[i + 1][j] |= dp[i][j - a[i]]
