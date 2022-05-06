import math

def solution(fees, records):
    answer = []
    car_time = {}
    car_sum = []
    inout_check = {}
    last_minute = 23 * 60 + 59

    for record in records:
        arr = record.split()
        hour, minute = map(int, arr[0].split(':'))
        sum_minute = int(hour * 60 + minute)

        if arr[2] == 'IN':  # 입차
            car_time[arr[1]] = sum_minute
            inout_check[arr[1]] = 1
        elif arr[2] == 'OUT':  # 출차
            car_sum.append([arr[1], abs(sum_minute - car_time[arr[1]])])
            inout_check[arr[1]] = 0
    #출차가 안된 차량은 23시59분으로 계산하여 주차 시간 계산
    for cars in inout_check:
        if inout_check[cars] == 1:
            car_sum.append([cars, abs(last_minute - car_time[cars])])

    #딕셔너리 값 초기화
    for cars in car_time:
        car_time[cars] = 0

    #자동차 번호별 시간 합계 계산
    for car_num, time in car_sum:
        car_time[car_num] += time
    #자동차 요금 계산
    for cars in car_time:
        #번호, 요금으로 append
        if car_time[cars] <= fees[0]:  # 기본시간 보다 작을 경우
            answer.append([cars, fees[1]])
        else:
            answer.append([cars, fees[1] + (math.ceil((car_time[cars] - fees[0]) / fees[2])) * fees[3]])

    #자동차 번호 오름차순 정렬
    answer.sort()

    return [result[1] for result in answer]