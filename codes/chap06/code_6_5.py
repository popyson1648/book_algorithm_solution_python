"""射撃王：最適化を判定問題へ

対応: 6.7
計算量: 時間 O(N log N log M)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap06/code_6_5.cpp
"""

import sys


def shooting_king(balloons):
    n = len(balloons)
    left = -1  # 高さ0を探索範囲に含めるため、下端を -1 にする。
    right = max(h + s * n for h, s in balloons)
    while right - left > 1:
        mid = (left + right) // 2
        # 高さmidを超えるまでに、それぞれの風船を割れるか判定する。
        deadlines = []
        ok = True
        for h, s in balloons:
            if mid < h:
                ok = False
                break
            # 前提: 上昇速度 s > 0。
            deadlines.append((mid - h) // s)
        if ok:
            # 割る期限が早い風船から順に処理できるか調べる。
            deadlines.sort()
            for i, deadline in enumerate(deadlines):
                # i番目の風船を割る時刻はi秒。期限を過ぎていれば実現できない。
                if deadline < i:
                    ok = False
        if ok:
            right = mid
        else:
            left = mid
    return right


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    print(shooting_king([(next(it), next(it)) for _ in range(n)]))


if __name__ == "__main__":
    main()
