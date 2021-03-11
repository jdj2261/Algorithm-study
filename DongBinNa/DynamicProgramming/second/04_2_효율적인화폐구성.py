"""
Date : 21년 3월 7일
Description : Algorithm Study
Title : 효율적인 화폐 구성(다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
2 15        5
2
3
"""
n, m = map(int, input().split())
data = list()
for _ in range(n):
    data.append(int(input()))

dp = [10001] * (m+1)
dp[0] = 0
for i in range(n):
    for j in range(data[i], m+1):
        if dp[j - data[i]] != 10001:
            dp[j] = min(dp[j], dp[j-data[i]] + 1)

print(dp[m] if dp[m] != 10001 else -1)


