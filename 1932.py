import sys
from collections import deque

read = sys.stdin.readline

n = int(read())

triangle = [list(map(int,read().split())) for _ in range(n)]
viisted = [ [0] * i for i in range(1,n+1) ]

dx = [1,1]
dy = [0,1]

queue = deque()
queue.append([0,0])
viisted[0][0] = triangle[0][0]

# 삼각형 꼭대기에서 내려오면서 더한 수의 최댓값을 구하는 문제
# BFS로 순회할때마다 visited에 합한 수의 최댓값이 들어가도록 구현하여 마지막 행에 최댓값을 구하면 됨
while queue:
    x,y = queue.popleft()
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < len(triangle[nx]):
            if viisted[nx][ny] == 0:
                tmp = viisted[x][y] + triangle[nx][ny]
                viisted[nx][ny] = tmp
                queue.append([nx,ny])
            else:
                tmp = viisted[x][y] + triangle[nx][ny]
                viisted[nx][ny] = max(tmp, viisted[nx][ny])

print(max(viisted[n-1]))