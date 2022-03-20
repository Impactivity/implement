import sys
from collections import deque

read = sys.stdin.readline

T = int(read())

for i in range(T):
    # 문서의 갯수 N , 몇번째로 출력되었는지 궁금한 문서의 큐에서 순서 M
    N, M = map(int, read().split())
    priority = list(map(int, read().split()))

    print_queue = deque()

    for i in range(len(priority)):
        print_queue.append((i,priority[i]))

    #우선순위 내림차순으로 정렬
    priority.sort(reverse=True)
    priority = deque(priority)

    cnt = 0
    is_True = False

    while priority:
        #현재 큐 최댓값
        maxnum = priority.popleft()
        cnt += 1
        for i in range(N):
            inx, num = print_queue.popleft()
            # 큐 첫번째 우선순위가 최댓값이라면
            if num == maxnum:
                # inx가 M과 같으면 cnt수 출력하고 종료
                if inx == M:
                    print(cnt)
                    is_True = True
                    break
                else:
                    break
            # 최댓값이 아닌경우에는 출력 순서가 뒤로 밀려난다.
            print_queue.append((inx,num))
        if is_True == True:
            break


