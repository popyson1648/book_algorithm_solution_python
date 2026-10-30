"""一致する要素の個数

対応: 章末問題3.2
計算量: 時間 O(N)、入力領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

import sys


def count_matches(a, value):
    counter = 0
    for x in a:
        if x == value:
            counter += 1
    return counter


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, value = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print(count_matches(a, value))


if __name__ == "__main__":
    main()
