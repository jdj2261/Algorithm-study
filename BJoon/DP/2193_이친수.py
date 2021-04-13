import sys
import time
input = sys.stdin.readline

n = int(input())
dp = [0,1,1]

for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])

start = time.time()
print(dp[-1])
print(time.time() - start)

start2 = time.time()
sys.stdout.write(str(dp[-1]))
print(time.time() - start2)