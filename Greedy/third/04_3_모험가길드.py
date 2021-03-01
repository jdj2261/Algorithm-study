"""
Date : 21년 3월 1일
Description : Algorithm Study 실전문제풀이 1
Title : 모험가 길드(Greedy) 
"""
"""
공포도가 X인 모험가는 반드시 X명 이상으로 구성해야 함.
N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하시오.

입력예시        출력예시
5               2
2 3 1 2 2
"""

n = int(input())

datas = list(map(int, input().split()))
datas.sort()
result = 0
count = 0
for data in datas:
    count += 1
    if data <= count:
        result += 1
        count = 0

print(result)