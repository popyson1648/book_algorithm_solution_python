"""大小関係を満たす最大ペア数

対応: 章末問題7.1
計算量: 時間 O(N log N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap07.md
"""

import sys


def match_count(a, b):
    a, b = sorted(a), sorted(b)
    i = 0
    for value in b:
        # 小さい値どうしから組にし、大きい値が必要な相手の候補を残す。
        if i < len(a) and a[i] < value:
            i += 1
    return i


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    b = [next(it) for _ in range(n)]
    print(match_count(a, b))


if __name__ == "__main__":
    main()
