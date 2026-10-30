"""年齢当てゲーム

対応: 6.5
計算量: 質問回数 O(log(R-L))、領域 O(1)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap06/code_6_3.cpp
"""




def main():
    print("Start Game!", flush=True)
    # 年齢の候補を半開区間 [left, right) で表す。
    left, right = 20, 36
    while right - left > 1:
        mid = left + (right - left) // 2
        print(f"Is the age less than {mid} ? (yes / no)", flush=True)
        answer = input().strip()
        if answer == "yes":
            right = mid
        else:
            left = mid
    print(f"The age is {left}!")


if __name__ == "__main__":
    main()
