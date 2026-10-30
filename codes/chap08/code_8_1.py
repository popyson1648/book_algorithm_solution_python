"""配列の参照と更新

対応: 8.2
計算量: 時間・領域 O(1)（固定長の例）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap08/code_8_1.cpp
"""




def main():
    a = [4, 3, 12, 7, 11, 1, 9, 8, 14, 6]
    print(a[0])
    print(a[2])
    a[2] = 5
    print(a[2])


if __name__ == "__main__":
    main()
