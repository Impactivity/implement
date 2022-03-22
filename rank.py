def solution(n, results):
    answer = 0

    wins = {}
    loses = {}

    for i in range(1,n+1):
        wins[i] = set()
        loses[i] = set()

    for i,j in results:
        wins[i].add(j) # i가 이긴 애들
        loses[j].add(i) # j가 진 애들


    for i in range(1,n+1):
        for winner in loses[i]: #i가 졌던 애들은
            wins[winner].update(wins[i]) #i가 이겼던 애들을 이긴다.
        for loser in wins[i]: #i가 이겼던 애들은
            loses[loser].update(loses[i]) #i가 졌던 애들한테도 진다.

    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            answer += 1


    return answer