"""
Date : 21년 3월 15일
Description : Algorithm Study 실전문제풀이 2
Title : 곱하기 혹은 더하기(Greedy) 
"""

"""
문자열 S가 주어졌을 때
왼쪽부터 오른쪽 곱하기 또는 더하기를 하여
만들어질 수 있는 수 중에 가장 큰 수 구하기 (사칙연산 규칙 무시)

입력예시1   입력예시2
02984       576

출력예시    출력예시2
576         210
"""

def multiply_or_sum(s: list) -> int:
    result = s[0]

    for i in range(1, len(s)):
        if s[i] <= 1 or result <=1:
            result += s[i]
        else:
            result *= s[i]
    return result

s = list(map(int, input()))
result = multiply_or_sum(s)

print(result)