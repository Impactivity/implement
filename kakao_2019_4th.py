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


test_case = [[[1,1,0], 1 ],
             [[30,10,4,1], 30],
             [[1,1,1], 6]
             ]

print(solution(test_case[0][0] ,test_case[0][1]))
