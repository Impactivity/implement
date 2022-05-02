import sys

read = sys.stdin.readline

while True:
    textline = list(map(str, read().rstrip()))

    if len(textline) == 1 and textline[0] == '.':
        break

    stack = []
    isTrue = True

    for text in textline:
        if text == '(' or text == '[':
            stack.append(text)

        elif text == ')' :
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                isTrue = False
                break
        elif text == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                isTrue = False
                break

    if len(stack) != 0:
        print('no')
    else:
        if isTrue == True:
            print('yes')
        else:
            print('no')

