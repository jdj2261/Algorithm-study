"""
Date : 21년 4월 18일
Description : Baekjoon 
Title : 타일채우기
"""
# 다시풀기
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[0] = 1

for i in range(0, n+1, 2):
    dp[i] += dp[i-2] * 3
    for j in range(i-4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[n])