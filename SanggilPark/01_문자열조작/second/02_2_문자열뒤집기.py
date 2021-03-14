"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 문자열 뒤집기 
"""
"""
https://leetcode.com/problems/reverse-string/
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    input_list =  ["h","e","l","l","o"]
    sol.reverseString(input_list)
    print(input_list)