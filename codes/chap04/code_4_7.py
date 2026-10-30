"""フィボナッチ数列の反復計算

対応: 4.3–4.4
計算量: N項まで時間 O(N)、領域 O(N)（算術演算回数）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_7.cpp
"""




def main():
    f = [0] * 50
    f[1] = 1
    for n in range(2, 50):
        f[n] = f[n - 1] + f[n - 2]
        print(f"{n} 項目: {f[n]}")


if __name__ == "__main__":
    main()
