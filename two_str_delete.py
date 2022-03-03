# 프로그래머스 짝지어 제거하기
# 같은 알파벳 2개 붙어있는 짝을 찾아 제거하는데 문자열 모두 제거 할 수 없으면 0
# 모두 제거하면 리턴 1
# keypoint : stack을 이용하여 스택 상단 값과 문자열 계속 비교한다.

def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return 0 if len(stack) else 1