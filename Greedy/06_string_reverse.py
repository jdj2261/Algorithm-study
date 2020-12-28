"""
Date : 20년 12월 22일
Description : Algorithm Study 실전문제풀이 3
Title : 문자열 뒤집기(Greedy) 
"""

"""
0과 1로만 이루어진 문자열 S
연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이고, 모두 같은 숫자로 만들기 위한 최소 횟수 구하기

입력예시    출력예시
0001100     1
"""

data = list(map(int, input("숫자입력: ")))

zero_cnt = 0
one_cnt = 0

if data[0] == 1:
    one_cnt += 1
else:
    zero_cnt += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == 1:
            one_cnt += 1
        else:
            zero_cnt += 1
        
print(min(one_cnt, zero_cnt))