"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 가장 긴 팰린드롬 부분 문자열
"""
"""
https://leetcode.com/problems/longest-palindromic-substring/
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i), expand(i, i+1), key=len)
        return result

if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    result = sol.longestPalindrome(s)
    print(result)