"""総和を求める再帰

対応: 4.1
計算量: 時間 O(N)、再帰領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_1.cpp
"""

def func(n):
    if n == 0:
        return 0
    return n + func(n - 1)
