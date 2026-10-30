"""括弧の対応をスタックで求める

対応: 章末問題9.3
計算量: 走査 O(N)、対応のソートを含めると O(N log N)、領域 O(N)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/solutions/chap09.md
"""

def check(s):
    # まだ対応する右括弧が見つかっていない左括弧の位置を保存する。
    stack = []
    pairs = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if not stack:
                print("error")
                return False
            # 右括弧は、直近の未対応の左括弧と組になる。
            pairs.append((stack.pop(), i))
    if stack:
        print("too many (")
        return False
    pairs.sort()
    print(", ".join(f"({a}, {b})" for a, b in pairs))
    return True


def main():
    check("((()())())")
    check("())")
    check("(()")


if __name__ == "__main__":
    main()
