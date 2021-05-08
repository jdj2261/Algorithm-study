"""
Date : 21. 05. 08
Title : 조합

https://leetcode.com/problems/combinations/
Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
"""

from typing import List
import itertools

class Solution:
    def combine1(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements.copy())

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
                
        dfs([], 1, k)
        return results

    def combine2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1), k))

if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 2
    result = sol.combine2(n, k)
    print(result)