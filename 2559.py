import sys

read = sys.stdin.readline

n,k = map(int, read().split())
arr = list(map(int,read().split()))

sum_list = []
psum = 0
for i in range(n):
    psum += arr[i]
    sum_list.append(psum)

_max = -float('inf')
for j in range(k-1,n):
    if j-k >= 0 :
        _max = max(_max, sum_list[j]-sum_list[j-k])
    else:
        _max = max(_max, sum_list[j])

print(_max)