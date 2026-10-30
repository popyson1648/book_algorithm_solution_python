"""必要個数を最小化する遷移

対応: 章末問題5.4・コード片
計算量: 1セルの更新 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

def transition(dp, a, i, j):
    # この要素を選ばない場合は、必要個数を引き継ぐ。
    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    # この要素を選ぶ場合は、残りの和を作る必要個数に1を加える。
    if j >= a[i]:
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - a[i]] + 1)
