"""
Date : 20년 2월 2일
Description : Algorithm Study
Title : 병사 배치하기(다이나믹 프로그래밍) 
"""
"""
입력 예시               출력 예시
7                       2
15 11 4 8 5 2 4
"""

# LIS 알고리즘
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp [i] = max(dp[i], dp[j] + 1)

print(n - max(dp))