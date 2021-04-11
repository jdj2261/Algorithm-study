"""
Date : 21년 4월 11일
Description : Algorithm Study
Title : 계단 오르기
"""
"""
https://leetcode.com/problems/climbing-stairs/

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

from collections import defaultdict
class Solution:
    dp = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]