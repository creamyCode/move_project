def solution(food_times, k):
    food_list = []
    food_cnt = len(food_times)
    for i in range(food_cnt):
        food_list.append((i + 1, food_times[i]))

    min_time = min(food_times)
    # 음식을 다먹는 시간보다 k가 클 경우 -1 리턴
    if sum(food_times) <= k:
        return -1
    # 한개의 음식을 다먹는데 걸리는 최소 시간 * 음식종류의 수 = 음식이 없어지기전 카운트, 해당 시간 이전일 경우는 음식수로 나눈 나머지 + 1을 하면 다음 먹을것
    if k < food_cnt * min_time:
        return (k % food_cnt) + 1
     
    # 음식이 없어지기 시작한 첫번째 경우까지 skip
    k -= food_cnt * min_time
    for i in range(food_cnt):
        food_list[i] -= min_time
    food_list = list(filter(lambda x:x[1] != 0, food_list))
    food_cnt = len(food_list)
    idx = 0
    while k != 0:
        if food_list[idx] == 0:
            food_list.pop(idx)
            food_cnt -= 1
        else:
            food_list[idx] -= 1
            k -= 1
        idx = (idx + 1) % food_cnt
    return 

print(solution([2, 2, 1], 4))


# 2 2 1 
# 4