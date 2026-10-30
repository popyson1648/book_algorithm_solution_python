"""フィボナッチ数列のメモ化

対応: 4.4
計算量: 時間 O(N)、領域 O(N)（算術演算回数）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_8.cpp
"""

def fibo(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # 計算済みなら保存した答えを使い、同じ計算を繰り返さない。
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]


def main():
    memo = [-1] * 50
    fibo(49, memo)
    # 0項目と1項目は直接返すため、メモには2項目以降が保存される。
    for n in range(2, 50):
        print(f"{n} 項目: {memo[n]}")


if __name__ == "__main__":
    main()
