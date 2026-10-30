"""番兵付き単方向連結リスト

対応: 8.3–8.4
計算量: 挿入・削除 O(1)、走査 O(N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap08/code_8_4.cpp
"""

class Node:
    def __init__(self, name=""):
        self.next = None
        self.name = name


nil = None


def init():
    global nil
    # 空リストでも番兵を置き、先頭・末尾を同じ手順で扱えるようにする。
    nil = Node()
    nil.next = nil


def print_list():
    cur = nil.next
    while cur is not nil:
        print(cur.name, end=" -> ")
        cur = cur.next
    print()


def insert(v, p=None):
    # デフォルト引数は定義時に評価されるため、実行時に番兵を選ぶ。
    if p is None:
        # 番兵の直後への挿入は、リストの先頭への挿入になる。
        p = nil
    v.next = p.next
    p.next = v


def main():
    init()
    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]
    for i, name in enumerate(names):
        insert(Node(name))
        print(f"step {i}: ", end="")
        print_list()


if __name__ == "__main__":
    main()
