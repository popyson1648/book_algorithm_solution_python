"""Shift Only

対応: 章末問題3.5
計算量: 時間 O(N log A)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

import sys


def how_many_times(n):
    if n <= 0:
        raise ValueError("正整数を指定してください")
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    return exponent


def shift_only(a):
    # 全要素を同時に割れる回数は、最も早く奇数になる要素で決まる。
    return min(how_many_times(x) for x in a)


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    print(shift_only(a))


if __name__ == "__main__":
    main()
