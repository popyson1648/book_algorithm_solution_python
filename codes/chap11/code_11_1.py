"""経路圧縮なしの根探索

対応: 11.2–11.5
計算量: 時間・再帰領域 O(木の高さ)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap11/code_11_1.cpp
"""

def root(par, x):
    if par[x] == -1:
        return x
    # 親をたどり、グループの代表となる根を探す。
    return root(par, par[x])
