"""クイックソート

対応: 12.5
計算量: 平均時間 O(N log N)、最悪時間 O(N²)、最悪再帰領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap12/code_12_3.cpp
"""

import sys


def quick_sort(a, left, right):
    # 対象は半開区間 [left, right)。要素が1個以下なら整列済み。
    if right - left <= 1:
        return
    pivot_index = (left + right) // 2
    pivot = a[pivot_index]
    a[pivot_index], a[right - 1] = a[right - 1], a[pivot_index]
    i = left
    # 基準値未満の要素を左に集める。iは次に詰める位置。
    for j in range(left, right - 1):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    # 基準値を境界に置くと、その位置が確定する。左右だけを再帰的に整列する。
    a[i], a[right - 1] = a[right - 1], a[i]
    quick_sort(a, left, i)
    quick_sort(a, i + 1, right)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    quick_sort(a, 0, n)


if __name__ == "__main__":
    main()
