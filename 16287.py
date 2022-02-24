# 백트레킹으로 주어진 배열에서 4개의 수를 뽑아 더하는 식으로
# 구현하였지만 , 시간초과 됨.

# import sys
#
# read= sys.stdin.readline
#
# w,n = map(int,read().split())
# arr = list(map(int,read().split()))
# visited = [0] * n
#
# def dfs(cnt, tot,depth):
#     if cnt == 4:
#         if tot == w:
#             print('YES')
#             exit(0)
#         else:
#             return False
#     else:
#         if tot >= w:
#             return False
#
#     for i in range(depth, n):
#         if visited[i] == 0:
#             visited[i] = 1
#             dfs(cnt+1, tot + arr[i], i )
#             visited[i] = 0
#
#     return False
#
#
# if dfs(0,0,0) == False:
#     print('NO')


import sys

input = sys.stdin.readline

w, n = map(int, input().split())
A = list(map(int, input().split()))
memoization = [False] * w

for i in range(n):

    # i inx에 해당하는 값과 그보다 큰 inx 값 두 수의 합을 구해서
    # w - A[i] - A[j] 값이 true 라는 것은
    # 현재 두 수 A[i], A[j]와 합해서 w를 만드는 수가 존재함을 의미.

    for j in range(i + 1, n):
        if A[i] + A[j] < w and memoization[w - A[i] - A[j]]:
            print("YES")
            sys.exit(0)

    # 0~i까지의 두 개의 수를 더해서 합이 w 보다 작다면
    # 두 수를 합한 값 inx에 True표시해줌.
    # 즉, 숫자 두개를 더해서 만들 수 있는 수 inx에 True를 표시하는 것이다.
    for j in range(i):
        if A[i] + A[j] < w:
            memoization[A[i] + A[j]] = True

print("NO")
