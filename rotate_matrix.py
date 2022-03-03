import math
#행렬 회전
def rotate(arr, st_rw, st_co, ed_rw, ed_co, _min):
    # 위쪽면 회전
    tmp = arr[st_rw - 1][st_co - 1]

    for i in range(st_co, ed_co):
        cur = arr[st_rw - 1][i]
        arr[st_rw - 1][i] = tmp
        tmp = cur
        _min = min(_min, cur)

    # 오른쪽면 회전
    for i in range(st_rw, ed_rw):
        cur = arr[i][ed_co - 1]
        arr[i][ed_co - 1] = tmp
        tmp = cur
        _min = min(_min, cur)

    # 아래쪽면 회전
    for i in range(ed_co - 2, st_co - 2, -1):
        cur = arr[ed_rw - 1][i]
        arr[ed_rw - 1][i] = tmp
        tmp = cur
        _min = min(_min, cur)

    # 왼쪽면 회전
    for i in range(ed_rw - 2, st_rw - 2, -1):
        cur = arr[i][st_co - 1]
        arr[i][st_co - 1] = tmp
        tmp = cur
        _min = min(_min, cur)

    return _min


def solution(rows, columns, queries):
    answer = []

    matrix = [[] * columns for _ in range(rows)]

    cnt = 1
    for i in range(0, rows):
        for j in range(0, columns):
            matrix[i].append(cnt)
            cnt += 1
    # 시작점 row , col, 끝점 row, col 이 주어진다.
    for ques in queries:
        _min = math.inf
        answer.append(rotate(matrix, ques[0], ques[1], ques[2], ques[3], _min))

    return answer