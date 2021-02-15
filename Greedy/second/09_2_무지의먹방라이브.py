"""
Date : 21년 2월 15일
Description : Algorithm Study 실전문제풀이 2
Title : 무지의 먹방 라이브(Greedy) 
"""
"""
food_times [3,1,2] 
k 5

0~1 초 1번 음식 [2,1,2]
1~2 초 2번 음식 [2,0,2]
2~3 초 3번 음식 [2,0,1]
3~4 초 1번 음식 [1,0,1]
4~5 초 3번 음식 [1,0,0]

k=5 초에서 방송 중단
장애 복구 후 1번 음식부터 다시 먹는다.

result 1
"""

"""
def solution(food_times, k):
    s_times = sorted(food_times)
    l_times = len(food_times)
    d_time = 0
    l_idx = 0
    for idx in range(l_times):
        if idx == 0:
            d_time += s_times[idx]*(l_times - idx)
        else:
            d_time += (s_times[idx]-s_times[idx-1])*(l_times - idx)
        if d_time > k:
            l_idx = idx -1
            break
        if d_time <= k:
            return -1
    lst = []
    for idx in range(l_times-1, -1, -1):
        if food_times[idx] > s_times[l_idx]:
            lst.append(idx+1)
    if len(lst) != 0:
    # 초과한 양만큼 뒤에서 순서를 세서 음식을 구합니다.
        return lst[(d_time - k -1) % len(lst)]
    else:
    # 모든 음식의 번호가 같은 경우, 전체에서 나머지 연산을 해서 결과를 구합니다.
        return k % l_times+1
"""

# 답안지 풀이
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_value = 0
    previous = 0
    
    length = len(food_times)
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]

import copy

# food_times = [3, 1, 2]
food_times = [1, 5, 1]
k = 6
time = 0
index = 0
result = copy.deepcopy(food_times)
while True:
    
    if time >= k:
        break

    for i in range(len(food_times)):
        if time >= k:
            break
        if food_times[i] == 0:
            # result[i] = food_times[i]
            time -= 1

            # index += 1
        else:
            result[i] = food_times[i]-1
            index = i
        time += 1

        print(result, time, index)
    food_times = result

print(index)

