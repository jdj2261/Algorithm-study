import sys
from collections import defaultdict
input = sys.stdin.readline


for tc in range(int(input())):
    dp = defaultdict(int)
    def add_one_two_three(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        if dp[n]:
            return dp[n]
        dp[n] = add_one_two_three(n-1) + add_one_two_three(n-2) + add_one_two_three(n-3)
        return dp[n]
    n = int(input())
    result = add_one_two_three(n)
    print(result)
