"""
Date : 20년 12월 29일
Description : Algorithm Study 예제 4-2
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

# 시 : 24
# 분 : 60
# 초 : 60

N = int(input("정수 N을 입력하세요: "))
count = 0
for hour in range(N+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour) + str(minute) + str(second):
                count += 1

print(count)