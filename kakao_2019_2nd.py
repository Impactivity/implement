from collections import Counter

def solution(stage_cnt, stages):
    arr = Counter(stages)
    tot = len(stages)

    answer = {}

    for i in range(1, stage_cnt + 1):
        if tot != 0:
            answer[i] = arr[i] / tot
            tot -= arr[i]
        else:
            answer[i] = 0

    answer = sorted(answer, key=lambda k: answer[k], reverse=True)

    return answer

# Counter를 쓰지 않고 구현

# def solution(N, stages):
#     result = {}
#     le = len(stages)
#
#     for i in range(1, N + 1):
#         if le != 0:
#             count = stages.count(i)
#             result[i] = count / le
#             le -= count
#         else:
#             result[i] = 0
#
#     result = sorted(result, key=lambda x: result[x], reverse=True)
#
#     return result
solution(5,[2, 1, 2, 6, 2, 4, 3, 3])