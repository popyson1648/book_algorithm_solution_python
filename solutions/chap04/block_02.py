"""トリボナッチのメモ化

対応: 章末問題4.2
計算量: 時間 O(N)、領域 O(N)（算術演算回数）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap04.md
"""

def func(n, memo):
    if n < 2:
        return 0
    if n == 2:
        return 1
    # 計算済みなら保存した答えを使い、同じ計算を繰り返さない。
    if memo[n] != -1:
        return memo[n]
    memo[n] = func(n - 1, memo) + func(n - 2, memo) + func(n - 3, memo)
    return memo[n]


def main():
    n = int(input())
    print(func(n, [-1] * (n + 1)))


if __name__ == "__main__":
    main()
