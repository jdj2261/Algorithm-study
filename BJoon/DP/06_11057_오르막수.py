import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

mod = 10007
for i in range(2, n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]

print(sum(dp[n]) % mod)

# 다른 풀이
import sys
N = int(sys.stdin.readline()) 
nums = [1] * 10 
mod = 10007 
for _ in range(N-1): 
    for i in range(1, 10): 
        nums[i] = (nums[i] + nums[i-1]) % mod 
sys.stdout.write(str(sum(nums) % mod))

