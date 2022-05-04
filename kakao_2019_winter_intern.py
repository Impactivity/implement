def solution(board, moves):
    row = len(board)
    stack = []
    answer = 0
    for i in moves:
        for j in range(row):
            if board[j][i-1]:
                if len(stack) > 0 and stack[-1] == board[j][i-1]:
                    stack.pop()
                    board[j][i-1] = 0
                    answer += 2
                else:
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                break
    return answer