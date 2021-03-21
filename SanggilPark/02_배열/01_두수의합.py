"""
Date : 21년 3월 15일
Description : Algorithm Study
Title : 두 수의 합
"""
"""
https://leetcode.com/problems/two-sum/

덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

class Solution:
    def twoSum(self, nums: list(int), target: int) -> list(int):
        result = []
        for i in range(len(nums)-1): 
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

# class Solution:
#     def twoSum1(self, nums: list[int], target: int) -> list[int]:
#         nums_map = {}
#         # 하나의 for 문으로 통합
#         for i, num in enumerate(nums):
#             if target - num in nums_map:
#                 return [nums_map[target - num], i]
#             nums_map[num] = i
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 4]
    target = 6
    print(sol.twoSum(nums, target))