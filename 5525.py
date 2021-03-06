import sys
import re

read = sys.stdin.readline

n = int(read())
m = int(read())
s = read()

answer, i, cnt = 0,0,0


#solution 1
while i < m-1 :
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n: # 제시된 문자열과 같을 경우, answer += 1 해주면서 cnt -= 1해준다. 맨앞에서 센거 빼고 다음에도 세야하므로
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)



#solution2 정규표현식 사용
ioi = re.findall('I(?:OI)+' , s)
count = 0

for k in ioi:
    # k를 2로 나누면 O의 갯수가 되는데 이는 IOI의 반복 횟수랑 같다.
    # 이것을 n으로 빼주고 + 1을 해준면 문자열 일치 갯수가 된다.
    l = len(k) // 2 - n + 1
    if l > 0:
        count += l

print(count)
