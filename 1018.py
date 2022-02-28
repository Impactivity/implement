import sys
import math
read = sys.stdin.readline

_min = math.inf


N,M = map(int, read().split())
graph = [list(map(str, read().strip())) for _ in range(m)]
answer = []

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if graph[k][l] != 'W':
                        first_W = first_W+1
                    if graph[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if graph[k][l] != 'B':
                        first_W = first_W+1
                    if graph[k][l] != 'W':
                        first_B = first_B + 1
        answer.append(first_W)
        answer.append(first_B)