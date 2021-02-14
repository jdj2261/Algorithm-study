"""
Date : 21년 2월 14일
Description : Algorithm Study 실전문제풀이 2
Title : 문자열 뒤집기(Greedy) 
"""

"""
0과 1로만 이루어진 문자열 S
연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이고, 모두 같은 숫자로 만들기 위한 최소 횟수 구하기

입력예시    출력예시
0001100     1
"""

s = list(map(int, input()))

zero2one_cnt = 0
one2zero_cnt = 0

compare_data = s[0]

for i in range(1, len(s)):
    if s[i] != compare_data:
        if s[i] == 0 :
            zero2one_cnt += 1
        else:
            one2zero_cnt += 1
        compare_data = s[i]

print(min(zero2one_cnt, one2zero_cnt))

    