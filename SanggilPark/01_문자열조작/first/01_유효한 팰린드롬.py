"""
Date : 21년 3월 11일
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

from typing import Collection, Deque


data = input()
input_data = []
for char in data:
    if char.isalnum():
        input_data.append(char.lower())

print(input_data)
n = len(input_data)

if n % 2 == 0:
    m = n // 2 - 1
else:
    m = n // 2 
print(input_data[:n//2], input_data[-1:m:-1])
if input_data[:n//2] == input_data[-1:m:-1]:
    print("true")
else:
    print("false")

# 풀이 1. 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

# 풀이 2. 데크 자료형을 이용한 최적화
import collections
def isPalindrome2(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

# 풀이 3. 슬라이싱 사용
import re
def isPalindrome3(self, s: str) -> bool:
    s = s.lower()

    s = re.sub('[^a-z0-9]','',s)
    return s == s[::-1]