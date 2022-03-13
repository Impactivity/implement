import sys
from collections import deque


read = sys.stdin.readline

test_cases = int(read())

for _ in range(test_cases):
    act = list(map(str,read().strip()))
    n = int(read()) # 배열의 갯수
    arr = read().rstrip()[1:-1].split(",")
    queue = deque(arr)
    flag = 0
    rev = 0

    if n == 0 :
        queue = []

    for i in act:
        if i == 'R':
            rev += 1

        elif i == 'D':
            if len(queue) < 1:
                print("error")
                flag = 1
                break
            else:
                if rev % 2 == 0:  # 뒤집기가 짝수번일때는 그대로 이기떄문에
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue)+"]")
        else:
            queue.reverse()
            print("[" + ",".join(queue)+"]")



