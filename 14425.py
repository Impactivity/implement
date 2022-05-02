import sys

read = sys.stdin.readline

n,m = map(int, read().split())

cnt = 0

arr = set([read().strip() for _ in range(n)])

for j in range(m):
    tmp_str = read().strip()
    if tmp_str in arr:
        cnt += 1

print(cnt)