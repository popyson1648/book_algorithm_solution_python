"""部分和問題のメモ化

対応: 章末問題4.6
計算量: 時間・領域 O(N(W+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap04.md
"""

import sys


def subset_sum(a, target):
    """a の要素と target は非負整数。"""
    memo = [[-1] * (target + 1) for _ in range(len(a) + 1)]

    def func(i, w):
        if w < 0:
            return False
        if i == 0:
            return w == 0
        # 先頭i個で和wを作れるかが計算済みなら再利用する。
        if memo[i][w] != -1:
            return bool(memo[i][w])
        # 最後の要素を選ばない場合と、選んで目標を減らす場合を試す。
        if func(i - 1, w) or func(i - 1, w - a[i - 1]):
            memo[i][w] = 1
        else:
            memo[i][w] = 0
        return bool(memo[i][w])

    return func(len(a), target)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, target = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if subset_sum(a, target) else "No")


if __name__ == "__main__":
    main()
