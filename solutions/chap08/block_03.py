"""単方向リストの削除

対応: 章末問題8.4・コード片
計算量: 直前のノードが既知なら時間・追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap08.md
"""

def erase(v, p, nil):
    # pは削除するノードの直前のノード。番兵は削除しない。
    if v is nil:
        return
    p.next = v.next
    v.next = None
