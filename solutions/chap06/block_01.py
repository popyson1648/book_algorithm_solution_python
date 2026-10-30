"""lower_boundの添字

対応: 章末問題6.1・コード片
計算量: 時間 O(log N)、領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap06.md
"""

from bisect import bisect_left


def rank_in_sorted(b, value):
    return bisect_left(b, value)
