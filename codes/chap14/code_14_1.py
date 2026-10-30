"""更新の有無を返す緩和

対応: 14.3
計算量: 時間・領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap14/code_14_1.cpp
"""

def chmin(a, b):
    """新しい値と更新フラグを返す。a, updated = chmin(a, b)。"""
    if a > b:
        return b, True
    return a, False
