"""
Date : 21년 2월 14일
Description : Algorithm Study 실전문제풀이 2
Title : 만들 수 없는 금액(Greedy) 
"""
"""
N개의 동전을 이용하여 만들 수 없는 양의 점수 금액 중 최솟값 구하기

입력 예시       출력예시
3 2 1 1 9       8
"""

n = int(input())
input_data = list(map(int, input().split()))
input_data.sort()

sum = input_data[0]
result = 0
for index, data in enumerate(input_data[1:]):
    if sum >= data:
        sum += data
    else:
        result = sum+1
print(result)

# 답안지 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)