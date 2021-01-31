
"""
Date : 20년 1월 31일
Description : Algorithm Study
Title : 바닥 공사(다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
3           5
"""

N = int(input())

d = [0] * 1001

d[0] = 1
d[1] = 3

for i in range(2, N):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[N-1])