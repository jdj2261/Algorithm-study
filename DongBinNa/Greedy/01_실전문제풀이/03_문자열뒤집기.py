"""
Date : 21년 3월 15일
Description : Algorithm Study 실전문제풀이 2
Title : 문자열 뒤집기(Greedy) 
"""

"""
0과 1로만 이루어진 문자열 S
연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이고, 모두 같은 숫자로 만들기 위한 최소 횟수 구하기

입력예시    출력예시
0001100     1
"""

input_data = list(map(int, input()))

result = input_data[0]
one_to_zero = 0
zero_to_one = 0

for i in range(1, len(input_data)):
    if result == 0 and input_data[i] == 1:
        zero_to_one += 1
        result = 1
    elif result == 1 and input_data[i] == 0:
        one_to_zero += 1
        result = 0

print(min(zero_to_one, one_to_zero))


