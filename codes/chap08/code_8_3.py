"""ノード直後への挿入

対応: 8.4
計算量: 時間・追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap08/code_8_3.cpp
"""

def insert(v, p):
    # v, p は next 属性を持つノード。p の次を先に保存する。
    v.next = p.next
    p.next = v
