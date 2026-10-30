"""2重ループの操作回数

対応: 2章・計算量
計算量: 時間 O(N^2)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap02/code_2_2.cpp
"""

def count_operations(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def main():
    n = int(input())
    count_operations(n)


if __name__ == "__main__":
    main()
