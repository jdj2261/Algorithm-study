"""
Date : 21년 2월 18일
Description : Algorithm Study 예제 4-1
Title : 시각(Implementation) 
"""
"""
00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중
3이 하나라도 포함되는 모든 경우의 수 구하기

입력 예시
5

출력 예시
11475
"""

n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)