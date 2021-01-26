"""
Date : 21년 1월 26일
Description : Algorithm Study 실전문제
Title : 카드 정렬하기(정렬) 
"""

"""
카드 묶음을 합했을 때 최소가 되려면 최소한 몇 번의 비교가 필요한가?
입력 예시       출력예시
3               100
10
20
40
"""
# 답안지에서는 heapq를 사용하라는데 아직 heapq를 모르니 나중에...

N = int(input())
input_data = []
for i in range(N):
    input_data.append(int(input()))

input_data.sort()

test = 0
result_list = []
for i in input_data:
    test += i
    result_list.append(test)
print(sum(result_list[1:]))