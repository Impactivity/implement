import sys

read = sys.stdin.readline

T = int(read())

#팩토리얼 구현
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


for i in range(T):
    n,m = map(int,read().split())
    arr = [i for i in range(m)]

    print( factorial(m) // ( factorial(m-n) * factorial(n) ) )

