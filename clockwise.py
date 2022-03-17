import sys
read = sys.stdin.readline

R,C = map(int,read().split())

graph = [ [0] * C for _ in range(R) ]

cnt = 1

for i in range(R):
    for j in range(C):
        graph[i][j] = cnt
        cnt += 1


def clockwise(s_x,s_y):
    # 우, 하, 좌 , 상
    # 오른쪽부터 가기 때문에 시작위치가 왼쪽 끝에어야 한다.
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = graph[s_x][s_y]
    tmp = graph[s_x+1][s_y]

    x, y = s_x, s_y

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]

        if x == s_x + 1 and y == s_y:
            break

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue

        graph[nx][ny], before = before, graph[nx][ny]
        x = nx
        y = ny

    graph[s_x][s_y] = tmp

    print(graph)

clockwise(0,0)


def inclockwise_rotate(s_x,s_y):

    mr, mc = s_x,s_y

    first_pos = graph[s_x][s_y]
    sec_pos = graph[R-1][0]
    third_pos = graph[R-1][C-1]

    #위쪽 로테이트
    for i in range(0,C-1):
        graph[0][i] = graph[0][i+1]

    #왼쪽 회전
    for i in range(R-1,0,-1):
        graph[i][0] = graph[i-1][0]
    graph[s_x + 1 ][0] = first_pos

    #아래 회전
    for i in range(C-1,0,-1):
        graph[R-1][i] = graph[R-1][i-1]
    graph[R-1][1] = sec_pos

    #오른쪽 회전
    for i in range(0, R-1):
        graph[i][C-1] = graph[i+1][C-1]

    graph[R-2][C-1] = third_pos

    print(graph)

    return

inclockwise_rotate(0,0)