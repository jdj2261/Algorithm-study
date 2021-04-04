"""
Date : 21년 4월 4일
Description : Algorithm Study 실전문제
Title : 떡볶이 떡 만들기(이진탐색) 
"""

"""
입력 예시           출력 예시
4 6
19 15 10 17         15
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0

start = 0
end = max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = start

print(start)