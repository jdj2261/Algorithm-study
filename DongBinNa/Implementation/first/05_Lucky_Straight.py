"""
Date : 21년 1월 1일
Description : Algorithm Study 실전문제
Title : 럭키 스트레이트(Implementation) 
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

input_data = list(input("숫자를 입력하세요: "))

left_term = []
right_term = []

for i in range(len(input_data)):
    if i < len(input_data)/2 :
        left_term.append(int(input_data[i]))
    else:
        right_term.append(int(input_data[i]))

left_sum = sum(left_term)
right_sum = sum(right_term)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

# 답안지 풀이
"""
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
"""
