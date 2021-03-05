"""
Date : 20년 3월 5일
Description : Algorithm Study
Title : 위에서 아래로 (정렬) 
"""
"""
입력 예시
3
15
27
12
"""    
# 내림차순 정렬

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

print(sorted(data, reverse=True))