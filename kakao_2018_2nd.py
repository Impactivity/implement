def solution(dartResult):
    pnt = {'S' : 1 , 'D' : 2, 'T' : 3}
    dartResult = dartResult.replace('10','A')

    answer = []
    for i in dartResult:

        if i.isdigit():
            answer.append(int(i))
        elif i in ('S', 'D', 'T'):
            point = answer.pop()
            answer.append(point ** pnt[i])
        elif i == 'A':
            answer.append(10)
        elif i == '*':
            if len(answer) >= 2 :
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2
        elif i == '#':
            point = answer.pop()
            answer.append(point * -1)

    return sum(answer)

solution('1S*2T*3S')