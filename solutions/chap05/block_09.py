"""個数制限なし部分和

対応: 章末問題5.5
計算量: 時間・領域 O(N(W+1))
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap05.md
"""

import sys


def subset_sum(a, target):
    dp = [[False] * (target + 1) for _ in range(len(a) + 1)]
    dp[0][0] = True
    for i in range(len(a)):
        # 和の小さい順に更新し、同じ要素を繰り返し選べるようにする。
        for j in range(target + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            # 同じ行の状態に1個追加するので、使用個数の制限はない。
            if j >= a[i] and dp[i + 1][j - a[i]]:
                dp[i + 1][j] = True
    return dp[-1][target]


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, target = next(it), next(it)
    a = [next(it) for _ in range(n)]
    print("Yes" if subset_sum(a, target) else "No")


if __name__ == "__main__":
    main()
