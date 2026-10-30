"""最初に一致する添字の探索

対応: 3.2
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap03/code_3_2.cpp
"""

import sys


def find_index(a, value):
    # 見つからなかった場合は、有効な添字と区別できる -1 を返す。
    found_id = -1
    for i in range(len(a)):
        if a[i] == value:
            found_id = i
            break
    return found_id


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, value = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print(find_index(a, value))


if __name__ == "__main__":
    main()
