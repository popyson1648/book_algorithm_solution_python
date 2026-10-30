"""スタックによる逆ポーランド記法の評価

対応: 章末問題9.2
計算量: 時間・領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap09.md
"""

def calc(expression):
    """空白なし・1桁の非負数・四則演算からなる正しい式を受け取る。"""
    stack = []
    for c in expression:
        if "0" <= c <= "9":
            stack.append(float(c))
        else:
            # 先に取り出す値が右辺、次が左辺。引き算・割り算では順序に注意する。
            a = stack.pop()
            b = stack.pop()
            if c == "+":
                stack.append(b + a)
            elif c == "-":
                stack.append(b - a)
            elif c == "*":
                stack.append(b * a)
            else:
                stack.append(b / a)
    return stack[-1]


def main():
    print(format(calc("34+12-*"), ".6g"))


if __name__ == "__main__":
    main()
