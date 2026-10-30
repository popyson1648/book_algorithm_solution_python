"""リングバッファによるキュー

対応: 9.2
計算量: 各操作 O(1)、領域 O(MAX)、実効容量 MAX-1
原文: https://github.com/drken1215/book_algorithm_solution/blob/bf4af1b13b6fb1f58b8a921ab319096422f064d6/codes/chap09/code_9_2.cpp
"""

MAX = 100000
qu = [0] * MAX
# headは取り出し位置、tailは次に格納する位置。末尾の次は先頭に戻る。
head = tail = 0


def init():
    global head, tail
    head = tail = 0


def is_empty():
    return head == tail


def is_full():
    # 空と満杯を区別するため、常に1枠空けておく。
    return head == (tail + 1) % MAX


def enqueue(x):
    global tail
    if is_full():
        print("error: queue is full.")
        return
    qu[tail] = x
    tail += 1
    if tail == MAX:
        tail = 0


def dequeue():
    global head
    if is_empty():
        print("error: queue is empty.")
        return -1
    result = qu[head]
    head += 1
    if head == MAX:
        head = 0
    return result


def main():
    init()
    enqueue(3)
    enqueue(5)
    enqueue(7)
    print(dequeue())
    print(dequeue())
    enqueue(9)


if __name__ == "__main__":
    main()
