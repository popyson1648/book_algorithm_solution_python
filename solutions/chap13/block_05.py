"""迷路の最短路

対応: 章末問題13.4
計算量: 時間・領域 O(HW)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap13.md
"""

import sys
from collections import deque


def maze_distance(field):
    h, w = len(field), len(field[0])
    start = goal = None
    for x in range(h):
        for y in range(w):
            if field[x][y] == "S":
                start = (x, y)
            if field[x][y] == "G":
                goal = (x, y)
    if start is None or goal is None:
        raise ValueError("SとGの両方が必要です")
    # 各マスまでの最短移動回数を記録する。-1はまだ到達していないマス。
    dist = [[-1] * w for _ in range(h)]
    dist[start[0]][start[1]] = 0
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if field[nx][ny] == "#" or dist[nx][ny] != -1:
                continue
            # 1歩で行けるマスを順に調べるので、初めて到達したときの距離が最短。
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
    return dist[goal[0]][goal[1]]


def main():
    it = iter(sys.stdin.read().split())
    h, w = int(next(it)), int(next(it))
    field = [next(it) for _ in range(h)]
    print(maze_distance(field))


if __name__ == "__main__":
    main()
