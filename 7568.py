import sys
read = sys.stdin.readline

# 자신보다 덩치가 큰 사람의 수를 출력하는 것으로
# 키와 몸무게 모두 커야 덩치가 큰것으로 정의한다.
# 문제의 key point는 자신보다 덩치가 큰 사람을 cnt 하면된다.
# [몸무게 , 키] 순으로 입력이 주어짐.
n = int(read())

person = [list(map(int, read().split())) for _ in range(n)]

cnt = [1] * n

for i in range(0,n):
    for j in range(0,n):
        if person[i][0] < person[j][0]:
            if person[i][1] < person[j][1]:
                cnt[i] += 1

print(*cnt)
