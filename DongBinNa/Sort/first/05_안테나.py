"""
Date : 21년 1월 26일
Description : Algorithm Study 실전문제
Title : 안테나(정렬) 
"""

"""
모든 집까지의 거리의 총합이 최소가 되도록 안테니 설치
입력 예시    출력 예시
4             5
5 1 7 9
"""

N = int(input())
locate = list(map(int, input().split()))
locate.sort()

distance = 0
result={}
for i in locate:
    for j in locate:
        distance += abs(i-j)    
    result[i] = distance
    distance = 0

min = 100000
w = 0
for key, val in result.items():
    if val < min:
        min = val
        w = key

print(w)


# 답안지 풀이
# 중간값에 해당하는 위치면 최소가 된다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])