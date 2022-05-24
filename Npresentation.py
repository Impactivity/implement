def solution(N, number):
    answer = -1
    # 8번 이하로 만들 수 있는 경우의 수 모두 구함
    dp = []
    for i in range(1, 9):
        all_cases = set()
        nums = int(str(N) * i)
        all_cases.add(nums)
        for j in range(0, i - 1):
            for op1 in dp[j]:
                for op2 in dp[-j - 1]:
                    all_cases.add(op1 + op2)
                    all_cases.add(op1 * op2)
                    all_cases.add(op1 - op2)
                    if op2 != 0:
                        all_cases.add(op1 // op2)

        if number in all_cases:
            answer = i
            break

        dp.append(all_cases)

    return answer

