"""
Date : 21년 3월 16일
Description : Algorithm Study
Title : 세 수의 합
"""
"""
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

class Solution:
    def threeSum(self, nums: list(int)) -> list(list(int)):
        result = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums) -2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) -1):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append((nums[i], nums[j], nums[k]))
        return result

class Solution:
    def threeSum2(self, nums: list(int)) -> list(list(int)):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0 인 경우이므로 정답 및 스킵 처리
                    results.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums [right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results
                    
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum2(nums))
        