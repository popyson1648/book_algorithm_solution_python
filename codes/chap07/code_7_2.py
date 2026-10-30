"""区間スケジューリング

対応: 7.3
計算量: 時間 O(N log N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap07/code_7_2.cpp
"""

import sys


def schedule(intervals):
    result = 0
    current_end_time = 0
    # 終了時刻が早い区間から選び、後の区間を選べる時間を残す。
    for start, end in sorted(intervals, key=lambda interval: interval[1]):
        # 最後に選んだ区間と重なるものは採用しない。
        if start < current_end_time:
            continue
        result += 1
        current_end_time = end
    return result


def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    print(schedule([(next(it), next(it)) for _ in range(n)]))


if __name__ == "__main__":
    main()
