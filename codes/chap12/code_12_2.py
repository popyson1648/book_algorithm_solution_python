"""マージソート

対応: 12.4
計算量: 時間 O(N log N)、追加領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap12/code_12_2.cpp
"""

import sys


def merge_sort(a, left, right):
    # 対象は半開区間 [left, right)。要素が1個以下なら整列済み。
    if right - left <= 1:
        return
    mid = left + (right - left) // 2
    merge_sort(a, left, mid)
    merge_sort(a, mid, right)
    # 右半分を逆順に格納し、バッファの両端から小さい値を取り出す。
    buf = [a[i] for i in range(left, mid)]
    buf.extend(a[i] for i in range(right - 1, mid - 1, -1))
    index_left, index_right = 0, len(buf) - 1
    for i in range(left, right):
        if buf[index_left] <= buf[index_right]:
            a[i] = buf[index_left]
            index_left += 1
        else:
            a[i] = buf[index_right]
            index_right -= 1


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    merge_sort(a, 0, n)


if __name__ == "__main__":
    main()
