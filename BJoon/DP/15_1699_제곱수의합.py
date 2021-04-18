# 다시 풀어보기
"""
Date : 21. 04. 17
"""
import sys
import time
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

now = time.time()
for i in range(1, n+1):
    for j in range(1, i//2+1):
        if j * j > i:
            break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(f'time : {time.time() - now}')
print(dp[n])