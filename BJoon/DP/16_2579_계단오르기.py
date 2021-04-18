"""
두번 째 칸 전에서 올라오거나
첫번째 칸 전에서 올라왔으면 셋째 칸 전에서 출발해야만 한다. (세번 연속 계단 오르는 것은 불가능 하므로)

dp[i] = max(dp[i-3] + array[i-1] + darray[i], dp[i-2]+array[i])
"""

import sys
input = sys.stdin.readline

n = int(input())
array = [0 for i in range(301)]
for i in range(n):
    array[i] = int(input())

dp = []
dp.append(array[0])
dp.append(array[0] + array[1])
dp.append(max(array[2]+array[0], array[2] + array[1]))
for i in range(3, n):
    dp.append(max(array[i]+dp[i-2], array[i]+array[i-1]+dp[i-3]))
print(dp[n-1])

# dp = [[0] * n]
# dp[0] = array[0]
# dp[1] = array[0] + array[1]
# dp[2] = max(array[2]+array[0], array[2]+array[1])
# for i in range(3, n):
#     dp[i] = max(array[i]+dp[i-2], array[i]+array[i-1]+dp[i-3])

# print(dp[n-1])