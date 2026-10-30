"""区間DPの分割点による緩和

対応: 章末問題5.9・疑似コード
計算量: 1区間の更新 O(j-i)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

def relax_interval(dp, prefix, i, j):
    # prefix[j] - prefix[i] は半開区間 [i, j) の和。
    # 最後に結合する2区間の境界をすべて試す。
    for k in range(i + 1, j):
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + prefix[j] - prefix[i])
