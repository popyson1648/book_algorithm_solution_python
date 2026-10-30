"""最大ヒープの実装

対応: 10.7
計算量: push/pop O(log N)、top O(1)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap10/code_10_5.cpp
"""

class Heap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        # 親が子以上になるまで、挿入した値を上へ移す。
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] >= x:
                break
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x

    def top(self):
        return self.heap[0] if self.heap else -1

    def pop(self):
        if not self.heap:
            return
        x = self.heap.pop()
        if not self.heap:
            return
        # 末尾の値を根から下へ移し、親が子以上になる位置を探す。
        i = 0
        while i * 2 + 1 < len(self.heap):
            child = i * 2 + 1
            # 大きい方の子を親に上げ、最大ヒープの条件を保つ。
            if child + 1 < len(self.heap) and self.heap[child + 1] > self.heap[child]:
                child += 1
            if self.heap[child] <= x:
                break
            self.heap[i] = self.heap[child]
            i = child
        self.heap[i] = x


def main():
    h = Heap()
    for x in (5, 3, 7, 1):
        h.push(x)
    print(h.top())
    h.pop()
    print(h.top())
    h.push(11)
    print(h.top())


if __name__ == "__main__":
    main()
