def solution(participant, completion):
    tmp = 0
    arr = {}

    for par in participant:
        arr[hash(par)] = par
        tmp += hash(par)

    for com in completion:
        tmp -= hash(com)

    return arr[tmp]


def solution2(participant, completion):
    participant_list = {}

    for name in participant:
        if name in participant_list:
            participant_list[name] += 1
        else:
            participant_list[name] = 1

    for name in completion:
        if name in participant_list:
            participant_list[name] -= 1

    return [name for name in participant_list if participant_list[name] > 0][0]