import sys

read = sys.stdin.readline

R,C,T = map(int, read().split())
graph = [ list(map(int,read().split())) for _ in range(R) ]

up = -1
down = -1

# 공기 청정기 위치 찾기
for i in range(R):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break


def spread():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    spread_arr = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1 and graph[i][j] != 0:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        spread_arr[nx][ny] += graph[i][j] // 5
                        tmp += graph[i][j] // 5
                graph[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            graph[i][j] += spread_arr[i][j]


# 공기청정기 위쪽 반시계방향으로 바람 이동
def air_up():
    # 우 상 좌 하
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 시계방향으로 바 이동
def air_down():
    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny




for i in range(T):
    spread()
    print(graph)
    air_up()
    print(graph)
    air_down()
    print(graph)


answer = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)



