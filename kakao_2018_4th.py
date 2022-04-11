def solution(n, t, m, timetable): # n : 셔틀버스 수 , t : 버스 시간 간격, m : 버스 정원, timetable : 기다리는 사람들
    #기다리는 사람들의 시간을 분 단위로 전환하여 오름차순으로 정렬한다.
    timetable = sorted([int(i[:2]) * 60 + int(i[3:]) for i in timetable])

    shuttle_bus = 540 #셔틀버스의 시간 9시부터
    con_time = 540 #콘이 가장 빨리 출근하는 시간 9시

    # 기존에 줄 서있는 크루들이 있다면 한명씩 태우고 n번째 셔틀버스 가장 마지막에 콘이 타야함.
    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= shuttle_bus:
                con_time = timetable.pop(0) - 1  #n번째 셔틀 마지막 한 자리에 들어가려면 현재 줄 선 사람보다 1분 빨라야함.
            else : #만약에 줄선 사람을 다넣고도 버스에 자리가 남는다면 콘의 출근시간은 셔틀버스 출발시간이됨.
                con_time = shuttle_bus
        shuttle_bus += t

    return f'{str(con_time // 60).zfill(2)}:{str(con_time % 60).zfill(2)}'


print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))