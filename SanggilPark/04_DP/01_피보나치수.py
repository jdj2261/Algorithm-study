"""
Date : 21년 4월 11일
Description : Algorithm Study
Title : 피보나치 수
"""
"""
https://leetcode.com/problems/fibonacci-number/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""
from collections import defaultdict
class Solution:
    # Tabolation
    dp = defaultdict(int)
    def fib_memoization(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib_memoization(n-1) + self.fib_memoization(n-2)
        return self.dp[n]

    def fib_tabolation(self, n: int) -> int:
        # self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        
        return self.dp[n]
    
    def fib_another(self, n: int) -> int:
        x, y = 0, 1
        for i in range(n):
            x, y = y, x+y
        return x

if __name__ == "__main__":
    sol = Solution()
    nums = 10
    # result = sol.fib_memoizatin(onums)
    # result = sol.fib_tabolation(nums)
    result = sol.fib_another(nums)
    print(result)
    # print(sol.fib_tabolation(nums))
