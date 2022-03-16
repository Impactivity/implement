import sys

read = sys.stdin.readline

n = int(read())

graph = [ [0] * n for _ in range(n) ]

# 좌 하 우 상
dx = [0,1,0,-1]
dy = [-1,0,1,0]

s_x, s_y = n // 2, n // 2

time = 0

for i in range( 2*n - 1 ):
    d =  i % 4

    if d == 0 or d == 2:
        time += 1

    for _ in range(time):
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]
        if 0 <= n_x < n and 0 <= n_y < n:
            graph[n_x][n_y] = graph[s_x][s_y] + 1
        s_x,s_y = n_x,n_y

print(graph)

