"""
Date : 20년 12월 23일
Description : Algorithm Study 실전문제풀이 5
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

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
ball = list(map(int, input().split()))
pick = list(combinations(ball, 2))
count = len(pick)

print(pick)

for a, b in pick:
    if a == b:
        count -= 1
print(count)

# import itertools
# N, M = map(int, input("N, M 입력하세요:").split())
# data = list(map(int, input("볼링공 무게 입력하세요: ").split()))
# data.sort()

# count = 0
# for i in range(len(data)-1):
#     if data[i] == data[i+1]:
#         count += 1 
#         if data[i-1] == data[i]:
#             count += 1

# result = N * (N-1) / 2 - count
# print(int(result))