"""3整数の和：一変数を消去

対応: 章末問題3.6
計算量: 時間 O((min(K,N)+1)²)、領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

import sys


def count_triples(k, n):
    count = 0
    for x in range(min(k, n) + 1):
        for y in range(min(k, n) + 1):
            # 2つの値を決めると、残りの1つは和の条件から一意に決まる。
            z = n - x - y
            if 0 <= z <= k:
                count += 1
    return count


def main():
    k, n = map(int, sys.stdin.buffer.read().split())
    print(count_triples(k, n))


if __name__ == "__main__":
    main()
