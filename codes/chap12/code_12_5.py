"""バケットソート（累積度数）

対応: 12.8
計算量: 時間・追加領域 O(N+MAX)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap12/code_12_5.cpp
"""

import sys


MAX = 100000


def bucket_sort(a):
    num = [0] * MAX
    for value in a:
        if not 0 <= value < MAX:
            raise ValueError("値は0以上MAX未満である必要があります")
        num[value] += 1
    # 各値以下の要素数を累積和で求め、並べ替え後の位置を決める。
    cumulative = [0] * MAX
    cumulative[0] = num[0]
    for value in range(1, MAX):
        cumulative[value] = cumulative[value - 1] + num[value]
    result = [0] * len(a)
    # 後ろから配置することで、同じ値どうしの元の順序を保つ。
    for i in range(len(a) - 1, -1, -1):
        cumulative[a[i]] -= 1
        result[cumulative[a[i]]] = a[i]
    a[:] = result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    a = [next(it) for _ in range(n)]
    bucket_sort(a)


if __name__ == "__main__":
    main()
