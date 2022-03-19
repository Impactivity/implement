import sys
from collections import deque

read = sys.stdin.readline

N,L,R = map(int,read().split())

arr = [ list(map(int,read().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

#bfs로 인접한 국가들중 국경선이 열린 국가 찾기
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    temp = [] #국경선 열린 방문한 국가
    temp.append((x,y))

    while queue :
        i,j = queue.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0:
                    diff = abs(arr[nx][ny] - arr[i][j])
                    if diff >= L and diff <= R:
                        queue.append((nx, ny))
                        temp.append((nx,ny))
                        visited[nx][ny] = 1


    return temp

cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    isTrue = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                temp = bfs(i,j)
                # 처음에 방문시작하는 국가를 append 하기때문에 1보다 커야
                # 연합국가들의 인구 합을 구할 수 있음.
                if len(temp) > 1:
                    isTrue = True
                    num = sum([ arr[x][y] for x,y in temp ]) // len(temp)
                    for x,y in temp:
                        arr[x][y] = num

    if isTrue == False:
        break
    cnt += 1


print(cnt)