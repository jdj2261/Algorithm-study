"""
Date : 21년 1월 27일
Description : Algorithm Study 실전문제
Title : 떡볶이 떡 만들기(이진탐색) 
"""

"""
입력 예시           출력 예시
4 6
19 15 10 17         15
"""

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1
print(result)


# def binary_search(array, target, start, end):
#     while (start <= end):
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None