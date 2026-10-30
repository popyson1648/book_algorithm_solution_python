"""連結リストの線形走査

対応: 章末問題8.1・コード片
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap08.md
"""

def print_list(nil):
    cur = nil.next
    while cur is not nil:
        print(cur.name, end=" -> ")
        cur = cur.next
    print()
