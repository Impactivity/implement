
import sys

read = sys.stdin.readline()

n = int(read())

graph = [ [0] * n for _ in range(n) ]

cnt = (n*n) // 4 + (n*n) % 4

clockwise = read().split()

# reverse는 dx 와 dy가 거꾸로
dx = [1,0,-1,0]
dy = [0,1,0,-1]

if clockwise == 'True':
    dx,dy = dy,dx


#각 소용돌이가 시작하는 방향
fir = 0
sec = 1
thr = 2
fou = 3

#1번 소용돌이 2번 소용돌이 3번 소용돌이 4번 소용돌이의 움직임을 작성
# 1번 0,0
# 2번 0,n-1
# 3번 n-1,0
# 4번 n-1,n-1
x1 = 0
y1 = 0

for i in range(1,cnt+1):

    nx = x1 + dx[fir % 4]
    ny = y1 + dy[fir % 4]
    if graph[nx][ny] == 0:
        graph[x1][y1] = i
    else:
        fir += 1










