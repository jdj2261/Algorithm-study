"""
Date : 21. 05. 05
Title : 섬의 개수

https://leetcode.com/problems/number-of-islands/

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x <= -1 or x >= len(grid) \
                or y <= -1 or y >= len(grid[0])\
                or grid[x][y] != '1':
                    return
            grid[x][y] = 0

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    result1 = sol.numIslands(grid)
    print(result1)