"""
Date : 21년 3월 15일
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

datas = list(map(int, input()))
n = len(datas)

left_sum, right_sum = 0, 0
for data in datas[:n//2]:
    left_sum += data
for data in datas[n//2:]:
    right_sum += data

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

