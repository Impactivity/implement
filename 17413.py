import sys
import re

read = sys.stdin.readline

arr = list(map(str, read().strip()))

i = 0
answer = []
while i < len(arr):

    if arr[i] == '<':
        start = i
        while arr[i] != '>':
            i += 1
        i += 1
    elif arr[i].isalnum():
        start = i
        while i < len(arr) and arr[i].isalnum():
            i += 1

        arr[start:i] = arr[start : i][::-1]
    else:
        i += 1

print("".join(arr))