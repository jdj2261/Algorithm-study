"""
Date : 21. 05. 07
Title : 순열

https://leetcode.com/problems/permutations/
Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

from itertools import dropwhile, permutations
from typing import List
from copy import deepcopy

class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))

    def permute2(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            print("elements: {}".format(elements))
            if len(elements) == 0:
                results.append(deepcopy(prev_elements))
                print(results)
                return
            
            for e in elements:
                next_elements = deepcopy(elements)
                next_elements.remove(e)
                prev_elements.append(e)
                print(f"dfs 이전 pre : {prev_elements}, next : {next_elements}, elements : {elements}, e:{e}")
                dfs(next_elements)
                prev_elements.pop()
                print("back")
                print(f"dfs 이후 pre : {prev_elements}, next : {next_elements}, elements : {elements}, e: {e}")
        dfs(nums)
        return results

if __name__ == "__main__":
    sol = Solution()
    digits = [0, 1]
    result = sol.permute2(digits)
    print(result)