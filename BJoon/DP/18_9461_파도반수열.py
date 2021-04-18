"""
Date : 21년 4월 19일
Description : Baekjoon 
Title : 파도반수열
"""
# 바로 맞춤
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for i in range(5, n+1):
        dp[i] = dp[i-5] + dp[i-1]
    print(dp[n])

