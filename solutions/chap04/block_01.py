"""トリボナッチの素朴な再帰

対応: 章末問題4.1
計算量: 時間 O(3^N)、再帰領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap04.md
"""

def func(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return func(n - 1) + func(n - 2) + func(n - 3)


def main():
    print(func(int(input())))


if __name__ == "__main__":
    main()
