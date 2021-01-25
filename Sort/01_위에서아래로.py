"""
Date : 20년 1월 25일
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
N = int(input())
input_list = []
for i in range(N):
    input_list.append(input())

input_list.sort(reverse=True)
print(input_list)
