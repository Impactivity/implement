#주어진 문제의 규칙은
# 1 -> 1 , 2 -> 2 , 3 -> 4 , 4 -> 11, 5 -> 12 , 6 -> 14
# 7 -> 21 , 8 -> 22 , 9->24, 10 -> 41로 숫자가 진행한다.
# 주어진 숫자가 3으로 나누어 떨어지지 않는 경우와 3으로 떨어지는 경우가 존재한다.
# 3으로 나누어 떨어지지 않을 때는 n을 3으로 계속 나눌때  나머지가 변환된 숫자가 됨을 알 수 있다.
# 나누어 떨어지는 경우에는 무조건 4가 변환된 숫자에 포함되고 그 몫을 -1 하여 다시 3으로 나누어 주고
# 위 과정을 반복하면 문제의 정답 도출이된다.

def solution(n):
    answer = ''

    while (n):
        if n % 3:
            answer += str(n % 3)
            n = n // 3
        else:
            answer += '4'
            n = n // 3 - 1
    # 계산된 방식에 따라 우측으로 문자열을 붙이기 때문에 역순으로 출력함
    return answer[::-1]