import sys
from collections import deque

read = sys.stdin.readline

top_arr = deque()

for _ in range(4):
    top_arr.append(deque(map(int,read().strip())))

rot_k = int(read())


def rotate(deq,dir):

    if dir > 0:
        tmp = deq.pop()
        deq.appendleft(tmp)
    else:
        tmp = deq.popleft()
        deq.append(tmp)

    return deq


for _ in range(rot_k):
    top_num, rot_dir = map(int,read().split())
    # 배열의 top1[2] <-> top2 [6] , top2[2] <-> top3[6] , top3[2] <-> top4[6] 번을 비교한다 .

    # 처음 톱니바퀴 번호 , 방향 백업
    tmp = top_num-1
    direct = rot_dir

    # 현재 톱니바퀴 2번 6번 백업
    tmp_2 = top_arr[tmp][2]
    tmp_6 = top_arr[tmp][6]

    # 오른쪽 톱니바퀴 회전
    while tmp < 3:
        if tmp_2 == top_arr[tmp+1][6]:
            break
        else:#오른쪽 대상 회전
            tmp_2 = top_arr[tmp + 1][2]
            top_arr[tmp+1] = rotate(top_arr[tmp+1],direct * -1)
            direct *= -1
            tmp+=1

    # 처음 톱니바퀴 번호 , 방향 백업
    tmp = top_num-1
    direct = rot_dir

    # 왼쪽 톱니바퀴 회전
    while tmp > 0:
        if tmp_6 == top_arr[tmp-1][2]:
            break
        else:#왼쪽 대상 회전
            tmp_6 = top_arr[tmp - 1][6]
            top_arr[tmp-1] = rotate(top_arr[tmp-1],direct * -1)
            direct *= -1
            tmp -= 1

    #문제 제시 톱니바퀴 회전
    rotate(top_arr[top_num-1],rot_dir)

# 12시방향 톱니바퀴 점수 합계 계산
tot = 0
for i in range(0,4):
    tot +=  ( top_arr[i][0] * ( 2 ** i ) )
print(tot)