"""K個以内の部分和：三次元DP

対応: 章末問題5.4・比較用コード片
計算量: 時間・領域 O(N(W+1)(K+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

def subset_sum_at_most_k(a, target, limit):
    # 「k個以内」なので、どのkでも空集合で和0を作れる。
    # dp[i][j][k] は先頭i個からk個以内を選んで和jを作れるかを表す。
    dp = [[[False] * (limit + 1) for _ in range(target + 1)]
          for _ in range(len(a) + 1)]
    for k in range(limit + 1):
        dp[0][0][k] = True
    for i in range(len(a)):
        for j in range(target + 1):
            for k in range(limit + 1):
                # この要素を選ばない場合。
                if dp[i][j][k]:
                    dp[i + 1][j][k] = True
                # この要素を選ぶ場合は、残りの和をk-1個以内で作る。
                if j >= a[i] and k >= 1 and dp[i][j - a[i]][k - 1]:
                    dp[i + 1][j][k] = True
    return dp[-1][target][limit]
