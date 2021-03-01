"""
Date : 21년 3월 1일
Description : Algorithm Study 실전문제풀이 2
Title : 볼링공 고르기(Greedy) 
"""
"""
두사람이 고를 수 있는 볼링공 번호의 조합 구하기


입력 예시1       출력예시1
5 3             8
1 3 2 3 2

입력 예시2          출력예시2
8 5                 25
1 5 4 3 2 4 5 2
"""
import time


n, m = map(int, input().split())
input_data = list(map(int, input().split()))
# input_data.sort()

start = time.time()
count = 0
for i in range(len(input_data)-1):
    for j in range(i + 1, len(input_data)):
        if input_data[i] != input_data[j]:
            count += 1

print(count)

print("걸린 시간 : ", (time.time() - start) * 100)
from itertools import combinations
start = time.time()
pick = list(combinations(input_data ,2))

count = 0
for a, b in pick:
    if a != b:
        count += 1
print("걸린 시간 : ", (time.time() - start) * 100)
print(count)