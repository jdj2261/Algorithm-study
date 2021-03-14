"""
Date : 21년 3월 14일
Description : Algorithm Study
Title : 유효한 팰린드롬 
"""
"""
https://leetcode.com/problems/valid-palindrome/
주어진 문자열이 팰린드롬인지 확인하라.
대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

입력
"A man, a plan, a canal: Panama"
출력 
true

입력
"race a car"
출력
false
"""

import re
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]
    
    def isPalindrome2(self, s: str) -> bool:
        strs: deque = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    result = sol.isPalindrome(s)
    result2 = sol.isPalindrome2(s)
    print(result2)