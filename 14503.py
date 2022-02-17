import sys
read = sys.stdin.readline

n,m = map(int, read().split())
x, y , d = map(int,read().split())
graph = [ list(map(int,read().split())) for _ in range(n) ]
visited = [[0]*m for _ in range(n)]


# dir 0:north, 1:east, 2:south, 3:west
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 1
visited[x][y] = 1 #처음시작하는곳 방문


while 1 :
    flag = 0
    #왼쪽부터 반시계방향으로 회전 0 3 2 1 순서로
    for i in range(4):
        nx = x + dx[(d+3)%4]
        ny = y + dy[(d+3)%4]
        d =(d+3) % 4 # 0 3 2 1 순서로 반복되는 식

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                cnt += 1
                x = nx
                y = ny
                flag = 1
                visited[nx][ny] = 1
                break
    if flag == 0 : #모든 방향을 돌 경우 후진
        if graph[x - dx[d]][y-dy[d]] == 1: #후진했는데 벽이면 cnt 출력 하고 종료
            print(cnt)
            break
        else: # 그렇지 않은 경우
            x = x-dx[d]
            y = y-dy[d]
