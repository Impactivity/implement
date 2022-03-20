import sys
from collections import deque

read = sys.stdin.readline

T = int(read())

for i in range(T):
    # 문서의 갯수 N , 몇번째로 출력되었는지 궁금한 문서의 큐에서 순서 M
    N,M = map(int, read().split())
    priority = list(map(int, read().split()))

    print_queue = deque(priority)
    m,cnt = M, 0

    while True:
        if print_queue[0] < max(print_queue):
            print_queue.append(print_queue.popleft())
            if 0 == m:
                m = len(print_queue) - 1
            else:
                m -= 1

        else:
            print_queue.popleft()
            cnt += 1
            if 0 == m:
                break
            else:
                m -= 1
    print(cnt)

