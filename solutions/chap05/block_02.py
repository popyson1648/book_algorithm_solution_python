"""0/1部分和の遷移

対応: 章末問題5.2・コード片
計算量: 1セルの更新 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

def transition(dp, a, i, j):
    # この要素を選ばない場合。
    if dp[i][j]:
        dp[i + 1][j] = True
    # この要素を選ぶ場合は、残りの和をそれ以前の要素で作る。
    if j >= a[i] and dp[i][j - a[i]]:
        dp[i + 1][j] = True
