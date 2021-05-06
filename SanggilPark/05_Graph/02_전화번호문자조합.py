"""
Date : 21. 05. 06
Title : 전화 번호 문자 조합

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # print(index, path)
            if len(path) == len(digits):
                result.append(path)
                # print("back tracking")
                return
        
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)
        
        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        return result      

if __name__ == "__main__":
    sol = Solution()
    digits = "234"
    result = sol.letterCombinations(digits)
    print(result)