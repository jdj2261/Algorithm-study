"""
Date : 20년 2월 18일
Description : Algorithm Study 실전문제
Title : 왕실의 나이트(Implementation) 
"""
"""
나이트가 이동할 수 있는 경우의 수 구하기
1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동
2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동

입력예시1 입력예시2 
a1      c2

출력예시1 출력예시2
c2       6
"""

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [
    (-2, -1), (-2, 1), 
    (-1, -2), (-1, 2), 
    (1, -2), (1, 2), 
    (2, -2), (2, 2)
]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


