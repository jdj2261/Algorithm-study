"""
Date : 20년 3월 7일
Description : Algorithm Study
Title : 개미 전사 (다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
4           8
1 3 1 5
"""

n = int(input())
array = list(map(int, input().split()))

dp = [0] * 100

dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(dp[n-1])


