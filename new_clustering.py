from collections import Counter
def solution(str1, str2):

    arr1 = list(map(str, str1))
    arr2 = list(map(str, str2))

    str_arr1 = []
    str_arr2 = []
    for i in range(len(arr1) - 1):
        if arr1[i].isalpha() and arr1[i + 1].isalpha():
            str_arr1.append(arr1[i].lower() + arr1[i + 1].lower())

    for i in range(len(arr2) - 1):
        if arr2[i].isalpha() and arr2[i + 1].isalpha():
            str_arr2.append(arr2[i].lower() + arr2[i + 1].lower())

    Counter1 = Counter(str_arr1)
    Counter2 = Counter(str_arr2)

    #합집합
    u = list((Counter1 | Counter2).elements())

    #교집합
    n = list((Counter1 & Counter2).elements())

    print(u,n)
    if len(u) == 0 and len(n) == 0:
        return 65536
    else:
        num = len(n) / len(u)
        num *= 65536

    return (int(num))