def solution(id_list, report, k):
    answer = []
    temp_id = {} #신고당한 사람 id
    src_id = {} #신고한 사람 id
    #중복 제거
    report = set(report)

    # 초기화
    for name in id_list:
        temp_id[name] = 0
        src_id[name] = 0

    # id별로 신고당한 건수, 신고한 건수
    for rep in report:
        src, dst = rep.split()
        temp_id[dst] += 1
        src_id[src] += 1

    # 리포트 별로 돌면서 신고당한 사람이 정지가 아닌 경우 하나씩 빼기
    for rep in report:
        src, dst = rep.split()
        if temp_id[dst] < k:
            if src_id[src] > 0:
                src_id[src] -= 1

    for _id in id_list:
        answer.append(src_id[_id])

    return answer