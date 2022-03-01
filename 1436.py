# 666, 6661, 6662, 6663 순서대로 증가하며 666이라는 숫자가 무조건 포함할때
# n번째로 작은 수를 출력하는문제

import sys

read = sys.stdin.readline

n = int(read())
six = 666
cnt = 0
# 브루트포스로 1씩더하면서 666이 포함한 숫자가 나올때마다 cnt + 1 해주면된다.
while True:
    if '666' in str(six):
        cnt += 1
    if cnt == n :
        break
    six += 1
print(six)