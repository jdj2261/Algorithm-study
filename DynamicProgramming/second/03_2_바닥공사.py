"""
Date : 21년 3월 7일
Description : Algorithm Study
Title : 바닥 공사(다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
3           5
"""

n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 3

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796

print(dp[n-1])


