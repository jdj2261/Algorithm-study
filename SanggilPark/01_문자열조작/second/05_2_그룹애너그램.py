"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 그룹 애너그램
"""
"""
https://leetcode.com/problems/group-anagrams/
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())

if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = sol.groupAnagrams(strs)
    print(result)