"""枚数制限付きコインの貪欲法

対応: 7.1–7.2
計算量: 時間 O(K)、領域 O(K)（ここではK=6）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap07/code_7_1.cpp
"""

import sys


VALUES = [500, 100, 50, 10, 5, 1]


def coin_count(amount, counts):
    result = 0
    # 金額の大きいコインから、残り金額と所持枚数の範囲で使う。
    for value, available in zip(VALUES, counts):
        add = min(amount // value, available)
        amount -= value * add
        result += add
    # 支払可能な入力を前提とする。
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    amount = next(it)
    print(coin_count(amount, [next(it) for _ in VALUES]))


if __name__ == "__main__":
    main()
