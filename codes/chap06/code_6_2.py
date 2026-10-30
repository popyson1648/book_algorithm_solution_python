"""単調な判定条件に対する二分探索

対応: 6.3–6.4
計算量: 判定 O(T) のとき時間 O(T log(R-L))、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap06/code_6_2.cpp
"""

def binary_search(predicate, left, right):
    """predicate(left)=False、predicate(right)=True、単調性を前提とする。"""
    # 左端は条件を満たさず、右端は満たす状態を保って境界を絞る。
    while right - left > 1:
        mid = left + (right - left) // 2
        if predicate(mid):
            right = mid
        else:
            left = mid
    return right
