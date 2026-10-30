"""3整数の和：三重ループ

対応: 章末問題3.6・比較用コード片
計算量: 時間 O((K+1)³)、領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

def count_triples(k, n):
    counter = 0
    for x in range(k + 1):
        for y in range(k + 1):
            for z in range(k + 1):
                if x + y + z == n:
                    counter += 1
    return counter
