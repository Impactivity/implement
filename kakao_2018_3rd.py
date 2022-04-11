from collections import deque

# remove를 사용했을 때
def solution1(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            print(cache)
            answer += 5

    return answer

# remove, deque maxlen 를 사용하지 않고 구현했을 때
def solution2(cacheSize, cities):
    answer = deque()
    temp = []
    cache_hit = 0

    for city in cities:
        city = city.lower()
        if city in answer:
            cache_hit += 1
            while answer[0] != city:
                temp.append(answer.popleft())
            answer.append(answer.popleft())
            while temp:
                answer.appendleft(temp.pop())
        else:
            if len(answer) == cacheSize and len(answer) != 0:
                answer.popleft()
                answer.append(city)
            elif len(answer) < cacheSize:
                answer.append(city)
            cache_hit += 5

    return cache_hit


print(solution2(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))