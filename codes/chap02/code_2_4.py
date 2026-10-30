"""最近点対の全探索

対応: 2.4
計算量: 時間 O(N²)、入力領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap02/code_2_4.cpp
"""

import math
import sys


def calc_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def closest_pair(points):
    minimum_dist = math.inf
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = calc_dist(*points[i], *points[j])
            if dist < minimum_dist:
                minimum_dist = dist
    return minimum_dist


def main():
    it = iter(sys.stdin.buffer.read().split())
    n = int(next(it))
    points = [(float(next(it)), float(next(it))) for _ in range(n)]
    print(format(closest_pair(points), ".6g"))


if __name__ == "__main__":
    main()
