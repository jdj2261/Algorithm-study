"""
Date : 21년 4월 11일
Description : Algorithm Study
Title : 집 도둑
"""
"""
https://leetcode.com/problems/house-robber/

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""
from typing import List
from collections import OrderedDict

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp.popitem()[1]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,1]
    result1 = sol.rob(nums)
    print(result1)
    
# nums = [1,3,1,5]
# n = len(nums)
# dp = [0] * (n)
# dp[0] = nums[0]
# dp[1] = max(nums[0], nums[1])

# for i in range(2, n):
#     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
# print(dp[-1])
