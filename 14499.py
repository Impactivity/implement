import sys
from collections import deque

read = sys.stdin.readline

n,m,x,y,k = map(int, read().split())

graph = [ list(map(int,read().split())) for _ in range(n) ]

# 동 : 1,  서 : 2 , 북 : 3, 남 : 4
order = deque(map(int,read().split()))

# 동, 서 ,북, 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 0 : 윗면, 1 : 동 ,2 : 서, 3: 북, 4 : 남, 5 :아랫먄

dice = [0 for _ in range(6)]

cur_floor = 1

while order:
    direct = order.popleft()

    nx = x + dx[direct-1]
    ny = y + dy[direct-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue

    if direct == 1: #동쪽
        dice[5], dice[2], dice[1], dice[0] = dice[1], dice[5], dice[0], dice[2]
    elif direct == 2: # 서쪽
        dice[5], dice[2], dice[1], dice[0] = dice[2], dice[0], dice[5], dice[1]
    elif direct == 3: # 북쪽
        dice[5], dice[3], dice[4], dice[0] = dice[3], dice[0], dice[5], dice[4]
    elif direct == 4: #남쪽
        dice[5], dice[3], dice[4], dice[0] = dice[4], dice[5], dice[0], dice[3]


    # 0이 아닐 경우 주사위 바닥 값을 지도의 값으로 세팅
    if graph[nx][ny] :
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    else: #0 이면 지도에 주사위 바닥값을 세팅
        graph[nx][ny] = dice[5]

    x,y = nx,ny
    print(dice[0])

