def solution(grid):
    answer = []
    row = len(grid)
    col = len(grid[0])

    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]

    # 상,우,하,좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for sx in range(row):
        for sy in range(col):
            for sd in range(4):
                if not visited[sx][sy][sd]:
                    visited[sx][sy][sd] = True
                    cnt = 0
                    nx, ny, d = sx, sy, sd
                    while True:
                        nx = (nx + dx[d]) % row
                        ny = (ny + dy[d]) % col
                        cnt += 1

                        if grid[nx][ny] == 'R':
                            d = (d + 1) % 4
                        elif grid[nx][ny] == 'L':
                            d = (d - 1) % 4

                        if visited[nx][ny][d]:
                            if (nx, ny, d) == (sx, sy, sd):
                                break
                            else:
                                cnt = 0
                                break
                        visited[nx][ny][d] = True

                    if cnt != 0:
                        answer.append(cnt)

    answer.sort()

    return answer