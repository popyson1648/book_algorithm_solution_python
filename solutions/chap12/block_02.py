"""Median of mediansによる選択

対応: 章末問題12.5・疑似コード
計算量: 最悪時間 O(N)、追加領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap12.md
"""

def select(a, k):
    """小さい順でk番目の値を返す（kは0始まり）。"""
    if not 0 <= k < len(a):
        raise ValueError("k は 0 以上 len(a) 未満にしてください")
    if len(a) <= 100:
        return sorted(a)[k]
    # 5個ずつのグループの中央値を集め、分割の基準値を選ぶ。
    medians = []
    for i in range(0, len(a), 5):
        group = sorted(a[i:i + 5])
        medians.append(group[len(group) // 2])
    median = select(medians, len(medians) // 2)
    # 基準値より小さい・等しい・大きいの3群に分ける。
    less, equal, greater = [], [], []
    for value in a:
        if value < median:
            less.append(value)
        elif value == median:
            equal.append(value)
        else:
            greater.append(value)
    if k < len(less):
        return select(less, k)
    if k < len(less) + len(equal):
        return median
    # 大きい群に進むときは、除いた2群の要素数だけ順位をずらす。
    return select(greater, k - len(less) - len(equal))
