def is_correct(p):
    dic = {'(': 0, ')': 0}
    for char in p:
        if char == ')':
            dic[')'] += 1
            if dic[')'] > dic['(']:
                return False
        elif char == '(':
            dic['('] += 1
    return True


# 문자열 p를 u, v로 분리하는 함수
def divide(p):
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]


def solution(p):
    # 1번
    if not p:
        return ""
    # 2번
    u, v = divide(p)

    # 3번
    if is_correct(u):
        return u + solution(v)  # 3-1
    else:  # 4번
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'

        # 4-4
        for i in range(1, len(u) - 1):
            if u[i] == ')':
                answer += '('
            else:
                answer += ')'

    return answer