import sys
read = sys.stdin.readline

t = int(read())

for i in range(t):
    h,w,n = map(int, read().split())

    #배정되는 방의 층, 거리 구하기
    if h >= n :
        floor = n # h 보다 작다면 n번째가 곧 층수가됨.
        distance = 1 # 무조건 1이다.
    else:
        if n%h == 0: # 나누어 떨어진다는 것은 무조건 꼭대기 층이다.
            floor = h
            distance = n // h
        else: #그렇지 않은경우 층으로 나눈 나머지가 현재 배정되는 층일것이다.
            floor = n % h
            distance = n // h + 1 # 몫으로 나누어 떨어지는 것은 꼭대기 층이기에, 몫 + 1이 배정되는 방의 거리가 될것이다.

    print(floor * 100 + distance )