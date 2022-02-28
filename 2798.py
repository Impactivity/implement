import sys
from itertools import combinations

read = sys.stdin.readline


n,m = map(int,read().split())
cards = list(map(int, read().split()))

#3장의 카드 코르는 경우의 수 조합
arr = list(combinations(cards,3))
_min = 999999
for ar in arr:
    if m >= sum(ar):
        if _min > m - sum(ar):
            _min = m - sum(ar)

print(m - _min)