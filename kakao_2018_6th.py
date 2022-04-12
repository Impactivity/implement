import numpy as np

def solution(m, n, board):
    arr = [list(i) for i in board]
    arr = np.array(arr)

    while True:
        delete = []

        for i in range(m - 1):
            for j in range(n - 1):
                if arr[i][j] != '_' and arr[i][j] == arr[i][j+1] and arr[i][j] == arr[i+1][j] and arr[i][j] == arr[i+1][j+1]:
                    delete.append([i,j])

        if not delete:
            break

        for i, j in delete:
            arr[i:i + 2, j:j + 2] = '_'

        # 제거되고 나서 블록 떨어뜨림
        # for k in range(m)을 추가한 것은, 모든 행을 검사해서 다 떨어 뜨리기 위함이다.
        # 2중 for 문으로만 구성하면 아래와 같이 됨. 따라서 행의 수 만큼 다시 반복하여 모두 처리해준다.
        # ["CCBDE",  ["___DE",
        #  "AAADE",   "____E",
        #  "AAABF",   "____F",
        #  "CCBBF"]   "___DF"]
        # 각 열을 조사하면서 떨어뜨리는 블록들 처리한다.
        for k in range(m):
            for j in range(n):
                for i in range(1, m):
                    if arr[i][j] == '_':
                        arr[i][j], arr[i - 1][j] = arr[i - 1][j], arr[i][j]
    answer = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '_':
                answer += 1

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))