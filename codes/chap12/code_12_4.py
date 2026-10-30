"""ヒープソート

対応: 12.6
計算量: 時間 O(N log N)、再帰領域 O(log N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap12/code_12_4.cpp
"""

import sys


def heapify(a, i, n):
    child = i * 2 + 1
    if child >= n:
        return
    if child + 1 < n and a[child + 1] > a[child]:
        child += 1
    if a[child] <= a[i]:
        return
    a[i], a[child] = a[child], a[i]
    heapify(a, child, n)


def heap_sort(a):
    n = len(a)
    # 子の部分木から順に整え、配列全体を最大ヒープにする。
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, i, n)
    # 最大値を末尾に確定し、残りの範囲を再びヒープにする。
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]  # 最大値を右詰め。
        heapify(a, 0, i)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    heap_sort(a)


if __name__ == "__main__":
    main()
