import sys
read = sys.stdin.readline

textline = list(map(str, read().strip()))

bomb_text = read().rstrip()

i = 0
stack = []

length = len(bomb_text)

# 특정 문자열을 삭제해야하는 경우, 별도 stack을 만들어서 삭제를 해준다.
# 끝 문자열을 비교해서 끝 문자 이전 bomb length 까지 모두 비교하여 bomb 문자열인지 검사
for char in textline:
    stack.append(char)
    if stack[-1] == bomb_text[-1] and ''.join(stack[-length:]) == bomb_text:
        del stack[-length:]


if len(stack) == 0:
    print('FRULA')
else :
    for i in stack:
        print(i,end='')

