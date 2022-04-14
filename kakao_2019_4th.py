def solution(food_times, k):
    answer = 0
    while k >= 0:
        if sum(food_times) <= k:
            return -1

        left_table = len(food_times) - food_times.count(0)
        rotate_cnt = k // left_table
        rotate_left = k % left_table

        # print('남은 회전수 : ' , k)
        # print(f'food_times : {food_times}, 마이너스 값 : {rotate_cnt} , 나머지 : {rotate_left}')
        #
        # 주어진 k수를 0을 제외한 table의 갯수 만큼 나누어서 몫 만큼 전부 빼준다음, 마이너스가 되는 대상들은
        # 나머지에 다시 더해준다.
        for inx, value in enumerate(food_times):
            if food_times[inx] != 0:
                food_times[inx] = value - rotate_cnt
                if food_times[inx] < 0 :
                    rotate_left -= food_times[inx]
                    food_times[inx] = 0
        k = rotate_left

        left_table = len(food_times) - food_times.count(0)
        # 실제 출력해야하는 answer 계산
        if k + 1 <= left_table:
            for i in food_times:
                answer += 1
                if i != 0:
                    k -= 1
                if k == -1:
                    return answer


# 이분탐색으로 풀이
# 모든 배열의 수를 mid초로 뺴고
# 음수가 되는 수들을 더할 때 (n * mid) + 음수인 값이
# k값이 된다는 것으로 아이디어 착안.

def solution2(food_times , k):
    l , r = 0, 1000000000

    #배열의 수, 전체 초를 빼는 수, 마지막 인덱스 도달하는 초
    n,cut,idx = len(food_times),0,0

    while l <= r:
        mid = (l+r) // 2 # Food_times의 모든 수를 mid로 빼면
        v = n * mid # 마지막 인덱스에 도달할 때는 n * mid 초가 된다.
        for f in food_times:
            tmp = f - mid
            if tmp < 0: #mid로 뺐을 때 음수가 되는 수들을 모두 더 해준 값이 실제 마지막 인덱스에 도달하는 초가 됨.
                v += tmp
        if v <= k:
            cut,idx = mid,v
            l = mid + 1
        else:
            r = mid - 1
    print(f'cut = {cut},idx = {idx}')
    food_times = [f-cut for f in food_times]
    for i in range(n):
        print(i,idx,k, food_times)
        if food_times[i] > 0 and idx == k:
            return i+1
        else :
            # 음수가
            if food_times[i] > 0:
                idx += 1

    return -1



test_case = [[[2,1,1], 3 ],
             [[30,10,4,1], 30],
             [[1,1,1], 6]
             ]

print(solution2(test_case[0][0] ,test_case[0][1]))
