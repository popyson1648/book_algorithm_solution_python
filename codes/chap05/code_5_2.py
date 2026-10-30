"""最小値への緩和

対応: 5.2–5.3
計算量: 時間 O(1)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap05/code_5_2.cpp
"""

def chmin(a, b):
    # Python の整数は変更不可。呼び出し側で a = chmin(a, b) と受け取る。
    if a > b:
        a = b
    return a
