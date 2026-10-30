"""配列による固定容量スタック

対応: 9.2
計算量: 各操作 O(1)、領域 O(MAX)
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap09/code_9_1.cpp
"""

MAX = 100000
st = [0] * MAX
# topは次に格納する位置。最後に入れた要素は、その1つ手前にある。
top = 0


def init():
    global top
    top = 0


def is_empty():
    return top == 0


def is_full():
    return top == MAX


def push(x):
    global top
    if is_full():
        print("error: stack is full.")
        return
    st[top] = x
    top += 1


def pop():
    global top
    if is_empty():
        print("error: stack is empty.")
        return -1
    top -= 1
    return st[top]


def main():
    init()
    push(3)
    push(5)
    push(7)
    print(pop())
    print(pop())
    push(9)


if __name__ == "__main__":
    main()
