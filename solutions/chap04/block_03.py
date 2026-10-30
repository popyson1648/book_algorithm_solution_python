"""753数の再帰列挙

対応: 章末問題4.5
計算量: D桁まで時間 O(3^D)、再帰領域 O(D)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap04.md
"""

def count_753(n, current=0, used=0):
    if current > n:
        return 0
    # 3つのビットで7・5・3の使用状況を記録し、すべて使った数だけ数える。
    counter = int(used == 0b111)
    # 末尾に7・5・3を1桁ずつ付け加えて探索する。
    counter += count_753(n, current * 10 + 7, used | 0b001)
    counter += count_753(n, current * 10 + 5, used | 0b010)
    counter += count_753(n, current * 10 + 3, used | 0b100)
    return counter


def main():
    print(count_753(int(input())))


if __name__ == "__main__":
    main()
