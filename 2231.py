import sys

read = sys.stdin.readline

n = int(read())

for j in range(1,n+1):
    num = j + sum(map(int, str(j))) #j + j 의 각 자리수 합
    if num == n:
        print(j)
        exit(0)
print(0)

