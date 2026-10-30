"""偶数の列挙

対応: 2.3
計算量: 時間 O(N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap02/code_2_3.cpp
"""




def main():
    n = int(input())
    for i in range(2, n + 1, 2):
        print(i)


if __name__ == "__main__":
    main()
