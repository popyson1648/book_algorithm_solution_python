"""部分和問題の再帰全探索

対応: 4.5
計算量: 時間 O(2^N)、再帰領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_9.cpp
"""

import sys


def func(i, w, a):
    # 選べる要素が残っていなければ、残りの目標が0のときだけ成功する。
    if i == 0:
        return w == 0
    # 最後の要素を選ばない場合。
    if func(i - 1, w, a):
        return True
    # 最後の要素を選ぶ場合は、その値を目標から差し引く。
    if func(i - 1, w - a[i - 1], a):
        return True
    return False


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, w = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if func(n, w, a) else "No")


if __name__ == "__main__":
    main()
