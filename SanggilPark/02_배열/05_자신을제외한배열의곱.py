"""
Date : 21년 3월 23일
Description : Algorithm Study
Title : 배열 파티션 1
"""
"""
https://leetcode.com/problems/product-of-array-except-self/

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List
# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1

    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    
    print(out)
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        print(p)
        out[i] = out[i] * p
        p = p * nums[i]

    return out

print(productExceptSelf([1,2,3,4]))