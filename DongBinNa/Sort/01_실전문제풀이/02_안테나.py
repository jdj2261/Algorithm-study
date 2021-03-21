"""
Date : 21년 3월 21일
Description : Algorithm Study 실전문제
Title : 안테나(정렬) 
"""

"""
모든 집까지의 거리의 총합이 최소가 되도록 안테니 설치
입력 예시    출력 예시
4             5
5 1 7 9
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])