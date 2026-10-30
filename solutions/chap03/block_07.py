"""たくさんの数式

対応: 章末問題3.7
計算量: 時間 O(N·2^N)、追加領域 O(1)（算術演算回数）
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap03.md
"""

def expression_sum(s):
    result = 0
    n = len(s)
    # 桁と桁の間ごとに「+」を入れるかどうかを選び、全通りを試す。
    for bit in range(1 << (n - 1)):
        tmp = 0
        for i in range(n - 1):
            tmp = tmp * 10 + int(s[i])
            # 「+」を入れる位置で、それまでにつないだ数を合計に加える。
            if bit & (1 << i):
                result += tmp
                tmp = 0
        # 最後の区切りから末尾までの数も加える。
        result += tmp * 10 + int(s[-1])
    return result


def main():
    print(expression_sum(input().strip()))


if __name__ == "__main__":
    main()
