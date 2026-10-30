"""単方向リストのノード

対応: 8.3
計算量: ノード作成 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap08/code_8_2.cpp
"""

class Node:
    def __init__(self, name=""):
        self.next = None
        self.name = name
