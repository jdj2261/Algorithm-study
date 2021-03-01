"""
Date : 20년 3월 1일
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

row = int(ord(input_data[0]) - ord('a')) + 1
column = int(input_data[1])

steps = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2),  (1, 2),
    (2, -1),  (2, 1)
]

count = 0
for step in steps:
    now_row = row + step[1]
    now_column = column + step[0]

    if now_row >= 1 and now_column >= 1 and now_row <= 8 and now_column <= 8:
        count += 1

print(count)