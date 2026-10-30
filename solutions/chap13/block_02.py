"""BFSによる連結成分数

対応: 章末問題13.1
計算量: 時間・領域 O(V+E)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap13.md
"""

import sys
from collections import deque


def count_components(graph):
    dist = [-1] * len(graph)
    result = 0
    # 未訪問の頂点から探索を始めるたび、新しい連結成分を1つ見つける。
    for start in range(len(graph)):
        if dist[start] != -1:
            continue
        dist[start] = 0
        queue = deque([start])
        while queue:
            v = queue.popleft()
            for next_v in graph[v]:
                if dist[next_v] != -1:
                    continue
                dist[next_v] = dist[v] + 1
                queue.append(next_v)
        result += 1
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(it), next(it)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = next(it), next(it)
        graph[a].append(b)
        graph[b].append(a)
    print(count_components(graph))


if __name__ == "__main__":
    main()
