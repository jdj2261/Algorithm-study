"""
Date : 20년 12월 22일
Description : Algorithm Study 실전문제풀이 2
Title : Multiply or Sum(Greedy) 
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

input_data = list(map(int,input("숫자를 입력하세요 : ")))
print(input_data)

result = input_data[0]

for index in range(1, len(input_data)):
    num = int(input_data[index])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num 
print(result)



