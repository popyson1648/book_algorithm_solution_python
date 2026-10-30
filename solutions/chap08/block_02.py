"""添字取得を繰り返す走査

対応: 章末問題8.2・比較用コード片
計算量: get(i) が O(i+1) なら全体 O(N²)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap08.md
"""

def print_by_index(n, get):
    """getは先頭からi番目を取得する関数。探索コストも比較対象。"""
    for i in range(n):
        print(get(i))
