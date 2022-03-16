from collections import Counter

def solution(genres, plays):
    answer = []
    dic = {}

    gen = list(Counter(genres))

    play_cnt = []

    # 장르별 플레이 수 합을 구함
    for tmp_gen in gen:
        _sum = 0
        for i in range(len(genres)):
            if genres[i] == tmp_gen:
                _sum += plays[i]

        play_cnt.append([tmp_gen,_sum])

    play_cnt = sorted(play_cnt, key=lambda k : k[1], reverse = True)

    print(play_cnt)

    # 장르별 플레이수
    arr = [ [] for _ in range(len(play_cnt)) ]

    for j in range(len(play_cnt)):
        for i in range(len(genres)):
            if genres[i] == play_cnt[j][0]:
                arr[j].append([plays[i],i])


    for i in range(len(arr)):
        arr[i] = sorted(arr[i], key = lambda k : k[0] , reverse = True)
        cnt = 0
        for j,inx in arr[i]:
            if cnt == 2:
                break
            else:
                answer.append(inx)
                cnt+=1

    return answer