"""再帰の呼び出しと復帰の観察

対応: 4.1
計算量: 時間 O(N)、再帰領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_2.cpp
"""

def func(n):
    print(f"func({n}) を呼び出しました")
    if n == 0:
        return 0
    result = n + func(n - 1)
    # 再帰呼び出しから戻る順に、求まった和を表示する。
    print(f"{n} までの和 = {result}")
    return result


def main():
    func(5)


if __name__ == "__main__":
    main()
