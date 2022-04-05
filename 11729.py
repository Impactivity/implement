import sys

read = sys.stdin.readline

n = int(read())

# 1,2,3 막대가 주어졌을 때
# 하노이탑을 옮기는 방법 3단계
# 1번에 있는 위에서 부터 n-1개 원판을 1번에서 2번으로 옮긴다.
# 마지막 n번째 원판을 1번에서 3번으로 옮긴다.
# 2번 막대에 있는 원판들을 3으로 옮긴다.

def hanoi(n,start,end):
    if n == 1:
        print(start,end)
        return
    hanoi(n-1,start,6-start-end)
    print(start,end)
    hanoi(n-1,6-start-end, end)

print(2 ** n - 1)
hanoi(n,1,3)