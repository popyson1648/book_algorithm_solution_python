"""フィボナッチ再帰の実行順序

対応: 4.3
計算量: 時間 O(2^N)、再帰領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap04/code_4_6.cpp
"""

def fibo(n):
    print(f"fibo({n}) を呼び出しました")
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = fibo(n - 1) + fibo(n - 2)
    # 2つの再帰呼び出しが終わってから、この項の値が確定する。
    print(f"{n} 項目 = {result}")
    return result


def main():
    fibo(6)


if __name__ == "__main__":
    main()
