"""部分和問題のビット全探索

対応: 3.5
計算量: 時間 O(N·2^N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap03/code_3_6.cpp
"""

import sys


def subset_sum(a, target):
    exist = False
    # 各ビットを要素を選ぶ・選ばないに対応させ、すべての部分集合を調べる。
    for bit in range(1 << len(a)):
        total = 0
        for i in range(len(a)):
            if bit & (1 << i):
                total += a[i]
        if total == target:
            exist = True
    return exist


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, target = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if subset_sum(a, target) else "No")


if __name__ == "__main__":
    main()
