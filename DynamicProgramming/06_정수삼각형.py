"""
Date : 20년 1월 31일
Description : Algorithm Study
Title : 정수삼각형(다이나믹 프로그래밍) 
"""
"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        
        dp[i][j] = dp[i][j] + max(up_left, up)
print(max(dp[n-1]))