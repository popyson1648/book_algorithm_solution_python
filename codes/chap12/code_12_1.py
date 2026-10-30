"""挿入ソート

対応: 12.3
計算量: 最悪時間 O(N²)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap12/code_12_1.cpp
"""

import sys


def insertion_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i
        # 左側の整列済み部分で、大きい値を右にずらして挿入位置を空ける。
        while j > 0:
            if a[j - 1] > value:
                a[j] = a[j - 1]
                j -= 1
            else:
                break
        a[j] = value


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    insertion_sort(a)


if __name__ == "__main__":
    main()
