import sys


read = sys.stdin.readline

n,m = map(int, read().split())

arr = set([read() for _ in range(n)])
cnt = 0
for _ in range(m):
    t = read()
    if t in arr:
        cnt += 1
print(cnt)

