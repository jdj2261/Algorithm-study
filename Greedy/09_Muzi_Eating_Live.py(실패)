"""
Date : 20년 12월 23일
Description : Algorithm Study 실전문제풀이 6
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

##실패!!!!!!!........

def solution(food_times, k):
    answer = 0
    cnt = 0
    for _ in range(k+1):
        if cnt >= len(food_times):
            cnt = 0  
            answer = 0
        cnt += 1
        if food_times[cnt-1] != 0:
            food_times[cnt-1] = food_times[cnt-1] - 1
        else:
            if sum(food_times) == 0:
                return -1
            if cnt < len(food_times):
                food_times[cnt] = food_times[cnt]-1
                cnt += 1
            else:
                cnt = 1
    answer = cnt

    return answer

food_times = list(map(int, input("food time을 입력하세요: ").split()))
k = int(input("중단된 시간을 입력하세요: "))

# cnt = 0
# for _ in range(k+1):
#     if cnt >= len(food_times):
#         cnt = 0  

#     cnt += 1

#     if food_times[cnt-1] != 0:
#         food_times[cnt-1] = food_times[cnt-1] - 1
#     else:
#         if cnt < len(food_times):
#             if food_times[cnt] == 0:
#                 print("finished")
#             else:
#                 food_times[cnt] = food_times[cnt]-1
#                 cnt += 1
#         else:
#             cnt = 1
#     print(food_times, cnt)
# answer = cnt
# print(answer)

result = solution(food_times, k)

print(result)
