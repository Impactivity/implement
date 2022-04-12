import re

def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    p = re.compile(r'[a-z]{2}',re.I)

    str1list = []
    str2list = []
    for i in range(len(str1)-1):
        tmp_str = str1[i] + str1[i+1]
        if p.findall(tmp_str):
            str1list.append(tmp_str)

    for i in range(len(str2)-1):
        tmp_str = str2[i] + str2[i+1]
        if p.findall(tmp_str):
            str2list.append(tmp_str)
    print(str1list,str2list)
    union = set(str1list) | set(str2list)
    inter = set(str1list) & set(str2list)

    union_add = 0
    inter_add = 0

    # 다중집합의 경우 서로 다른 두 집합에서 교집합의 수는
    # 중복되는 원소의 갯수가 더 적은 집합의 원소 갯수가 된다.
    # 예를들어, {AA,AA,AA,AA} {AA,AA} 인 경우, 갯수가 더 적은 집합의 원소 갯수인 교집합 갯수는 2이다.
    for i in inter:
        if str1list.count(i) > 1 and str2list.count(i) > 1:
            if str1list.count(i) > str2list.count(i):
                inter_add += str2list.count(i) - 1
            else:
                inter_add += str1list.count(i) - 1

    # 합집합의 갯수는 그 반대 이다.
    for i in union:
        if str1list.count(i) > 1 or str2list.count(i) > 1:
            if str1list.count(i) > str2list.count(i):
                union_add += str1list.count(i) - 1
            else:
                union_add += str2list.count(i) - 1

    if (len(union) + union_add) == 0:
        return 65536
    return int((len(inter) + inter_add) / (len(union) + union_add) * 65536)




# solution 2
# Counter를 사용하여 풀이

from collections import Counter
def solution2(str1, str2):

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