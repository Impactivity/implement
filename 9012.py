import sys
read = sys.stdin.readline

n = int(read())

for i in range(n):
    arr = list(map(str,read().strip()))

    stack = []
    is_vps = True
    for l in arr:
        if l == '(':
           stack.append('(')
        else:
            if len(stack) >= 1:
                stack.pop()
            else:
                is_vps = False
                break

    if is_vps == True and len(stack) == 0:
        print('YES')
    else:
        print('NO')
