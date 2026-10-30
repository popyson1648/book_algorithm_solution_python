"""ユークリッドの互除法

対応: 4.2
計算量: 時間・再帰領域 O(log min(M,N))（正整数）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_4.cpp
"""

def gcd(m, n):
    if n == 0:
        return m
    # 大きい方を余りに置き換えても、最大公約数は変わらない。
    return gcd(n, m % n)


def main():
    print(gcd(51, 15))
    print(gcd(15, 51))


if __name__ == "__main__":
    main()
