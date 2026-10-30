"""Aggressive cows：最小間隔の最大化

対応: 章末問題6.4
計算量: 時間 O(N log N+N log(A+1))、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap06.md
"""

import sys


def maximum_spacing(a, count):
    """2 <= count <= len(a)。Aは最大座標差。"""
    a = sorted(a)
    left, right = 0, a[-1] - a[0] + 1
    # すべての間隔を指定値以上にして、必要な個数を選べるかで二分探索する。
    while right - left > 1:
        distance = (left + right) // 2
        chosen, previous = 1, 0
        for i in range(1, len(a)):
            # 間隔を満たす最も左の位置を選び、残りを置く余地を広く残す。
            if a[i] - a[previous] >= distance:
                chosen += 1
                previous = i
        if chosen >= count:
            left = distance
        else:
            right = distance
    return left


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, count = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print(maximum_spacing(a, count))


if __name__ == "__main__":
    main()
