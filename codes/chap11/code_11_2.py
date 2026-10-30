"""経路圧縮付きの根探索

対応: 11.5
計算量: 1回の時間・再帰領域 O(木の高さ)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap11/code_11_2.cpp
"""

def root(par, x):
    if par[x] == -1:
        return x
    # 経路圧縮：親を直接根につなぎ直し、次回以降の探索を短くする。
    par[x] = root(par, par[x])
    return par[x]
