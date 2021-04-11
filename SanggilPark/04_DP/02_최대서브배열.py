"""
Date : 21년 4월 11일
Description : Algorithm Study
Title : 최대 서브 배열
"""
"""
https://leetcode.com/problems/maximum-subarray/

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

from typing import List
import sys
class Solution:
    def maxSubArray_memo(self, nums: List[int]) -> int:
        # 메모이제이션
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)
    
    def maxSubArray_Kadane(self, nums: List[int]) -> int:
        # 카데인 알고리즘
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result1 = sol.maxSubArray_memo(nums)
    print(result1)

    # result2 = sol.maxSubArray_Kadane(nums)
    # print(result2)