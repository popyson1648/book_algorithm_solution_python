"""配列の二分探索

対応: 6.1
計算量: 時間 O(log N)、追加領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap06/code_6_1.cpp
"""

A = [3, 5, 8, 10, 14, 17, 21, 39]


def binary_search(key, a=A):
    # 候補は両端を含む区間 [left, right]。見つからなければ -1 を返す。
    left, right = 0, len(a) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if a[mid] == key:
            return mid
        if a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    for key in (10, 3, 39, -100, 9, 100):
        print(binary_search(key))


if __name__ == "__main__":
    main()
