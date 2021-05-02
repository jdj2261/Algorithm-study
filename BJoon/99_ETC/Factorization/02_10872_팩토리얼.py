"""
Date : 21. 05. 02
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

출력
첫째 줄에 N!을 출력한다.

예제 입력 1 
10
예제 출력 1 
3628800
예제 입력 2 
0
예제 출력 2 
1
"""
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[0] = 1
if n != 0:
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] * (i)
print(dp[n])

# 다른 풀이
d=1
for i in range(1,int(input())):
    d*=i+1
print(d)