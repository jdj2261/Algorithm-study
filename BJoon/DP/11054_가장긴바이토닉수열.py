import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
left_dp = [1] * n
right_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[j] < array[i]:
            left_dp[i] = max(left_dp[i], left_dp[j]+1)

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if array[j] < array[i]:
            right_dp[i] = max(right_dp[i], right_dp[j] + 1)

dp = [left_dp[i] + right_dp[i] for i in range(n)]
print(max(dp) - 1)