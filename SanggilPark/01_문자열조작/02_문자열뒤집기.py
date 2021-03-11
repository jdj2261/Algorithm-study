"""
Date : 21년 3월 12일
Description : Algorithm Study
Title : 문자열 뒤집기 
"""
"""
https://leetcode.com/problems/reverse-string/
"""
data = list(input())
print(data[::-1])

# 풀이 1. 투포인터를 이용한 스왑
def reverseString(self, s: list[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 풀이 2. 파이썬다운 방식
def reverseString2(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # 1
    s.reverse()
    # 2
    s[:] = s[::-1]