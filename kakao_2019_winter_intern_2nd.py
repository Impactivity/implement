def solution1(s):
    s = list(map(str, s.strip()))
    temp_list = []
    total_list = []
    temp_str = ''
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            temp_list = []
            continue
        elif s[i] == '}':
            if s[i - 1].isnumeric():
                temp_list.append(int(temp_str))
                temp_str = ''
            total_list.append(temp_list)
        elif s[i] == ',':
            if s[i - 1].isnumeric():
                temp_list.append(int(temp_str))
                temp_str = ''
            continue
        else:
            if s[i - 1].isnumeric():
                temp_str += s[i]
            else:
                temp_str = s[i]

    total_list.sort(key=len)

    answer = []
    answer.append(total_list[0][0])

    for i in range(1, len(total_list)):
        for num in total_list[i]:
            if num not in answer:
                answer.append(num)

    return answer


##########################################
# 정규 표현식을 이용하여 풀이
##########################################
import re
from collections import Counter


def solution2(s):

    s = Counter(re.findall('\d+', s))
    print(s)
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))