"""
Date : 21. 04. 04
Title : 문자열 뒤집기
"""

s = list(map(int, input()))

zero2one = 0
one2zero = 0

compare_value = s[0]

if compare_value == 0:
    zero2one += 1
else:
    one2zero += 1

for i in range(1, len(s)):
    if s[i] != compare_value:
        if s[i] == 0:
            zero2one += 1
        else:
            one2zero += 1
    compare_value = s[i]

result = min(one2zero, zero2one)
print(result)
