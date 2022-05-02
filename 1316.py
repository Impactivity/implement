import sys
read = sys.stdin.readline

n = int(read())
arr = [read().strip() for _ in range(n)]

cnt = 0
for string in arr:
    bag = []
    is_true = True
    for a in range(len(string)):
        if string[a] in bag:
            if a >= 1:
                if string[a-1] == string[a]:
                    is_true = True
                else:
                    is_true = False
                    break
        else:
            bag.append(string[a])

    if is_true == True:
        cnt += 1
print(cnt)