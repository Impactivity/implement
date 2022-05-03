import sys
read = sys.stdin.readline

text_line = read().rstrip()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=', 'z=']

# solution 1
length = len(text_line)

cnt = 0
i = 0
while i < length:
    if text_line[i:i+2] in alpha:
        cnt += 1
        i += 2
    elif text_line[i:i+3] in alpha:
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt )


# solution 2
for i in alpha:
    text_line = text_line.replace(i,'*')

print(len(text_line))