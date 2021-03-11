"""
Date : 21년 2월 20일
Description : Algorithm Study 실전문제
Title : 게임 개발(Implementation) 
"""
"""
자릿수를 기준으로 점수 N을 반으로 나누어
왼쪽과 오른쪽 각 자리 수 합을 더해
같으면 LUCKY
다르면 READY 출력

입력예시        출력예시
123402        LUCKY

입력예시        출력예시
7755          READY
"""
input_data = list(input())
len = int(len(input_data)/2)
print(len)

first_sum = 0
second_sum = 0

for data in input_data[:len]:
    first_sum += int(data)

for data in input_data[len:]:
    second_sum += int(data)

if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")
