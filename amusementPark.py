#solution 1
import sys
import numpy as np

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N, K = map(int, read().split())
    least_cnt = N * N
    graph = [list(map(int, read().split())) for _ in range(N)]
    graph = np.array(graph)

    for i in range(N - K + 1):
        for j in range(N - K + 1):
            least_cnt = min(least_cnt, np.array(graph[i:i + K, j:j + K]).sum())

    print(least_cnt)


# solution 2
import sys
read = sys.stdin.readline
T = int(read())
for _ in range(T):
    N, K = map(int, read().split())
    least_cnt = N * N
    graph = [list(map(int, read().split())) for _ in range(N)]

    for i in range(N - K + 1):
        for a in range(N - K + 1):
            cnt = 0
            for r in range(i, i+K):
                for j in range(a , a + K):
                    if graph[r][j] == 1:
                        cnt += 1
            least_cnt = min(cnt, least_cnt )


    print(least_cnt)