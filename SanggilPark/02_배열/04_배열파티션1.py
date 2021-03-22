"""
Date : 21년 3월 17일
Description : Algorithm Study
Title : 배열 파티션 1
"""
"""
https://leetcode.com/problems/array-partition-i/

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
"""

class Solution:
    # 오름차순 풀이
    def arrayPairSum(self, nums: list(int)) -> int:
        sum = 0
        pair = []
        nums.sort()
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum

    # 짝수 번째 값 계산
    def arrayPairSum2(self, nums: list(int)) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum
    
    # 파이써닉
    def arrayPairSum3(self, nums: list(int)]) -> int:
        return sum(sorted(nums)[::2])

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 4, 3, 2]
    print(sol.arrayPairSum(nums))
    print(sol.arrayPairSum2(nums))
    print(sol.arrayPairSum3(nums))