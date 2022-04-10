import sys

read = sys.stdin.readline
# problem 1 ) n이 주어질 때 8의 갯수 카운팅
n = int(read())

# solution 1
answer1 = str(n).count('8')
print(answer1)

#solution 2
cnt = 0
arr2 = str(n)
for i in range(len(arr2)):
    if arr2[i] == '8':
        cnt += 1
print(cnt)

#problem 2 : 1부터 10000수까지 8의 갯수를 구하라
answer3 = str(list(range(1,10001))).count('8')

print(answer3)