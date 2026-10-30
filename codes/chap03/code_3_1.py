"""線形探索による存在判定

対応: 3.2
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap03/code_3_1.cpp
"""

import sys


def contains(a, value):
    exist = False
    for x in a:
        if x == value:
            exist = True
    return exist


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, value = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if contains(a, value) else "No")


if __name__ == "__main__":
    main()
