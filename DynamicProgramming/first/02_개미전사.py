
"""
Date : 20년 1월 31일
Description : Algorithm Study
Title : 개미 전사 (다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
4           8
1 3 1 5
"""

N = int(input())
input_data = list(map(int, input().split()))

# 1 3 1 5
D = [0] * 100

D[0] = input_data[0]
D[1] = max(input_data[0],input_data[1])

for i in range(2, N):
    D[i] = max(D[i-1], D[i-2] + input_data[i])

print(D[N-1])