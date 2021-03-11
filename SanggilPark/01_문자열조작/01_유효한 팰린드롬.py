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
