"""
Date : 21년 1월 27일
Description : Algorithm Study 실전문제
Title : 정렬된 배열에서 특정 수의 개수 구하기(이진탐색) 
"""
"""
입력 예시           출력 예시
4 6
19 15 10 17         15
"""
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().spllit()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)