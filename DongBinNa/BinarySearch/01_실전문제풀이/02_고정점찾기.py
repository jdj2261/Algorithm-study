"""
Date : 21년 3월 22일
Description : Algorithm Study 실전문제
Title : 고정점 찾기(이진탐색) 
"""
"""
입력 예시           출력 예시
5   
-15 -6 1 3 7        2
"""

n = int(input())
array = list(map(int, input().split()))

start = 0
end = len(array) - 1

def find_fix_spot(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid        
        if array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

index = find_fix_spot(array, start, end)

if index == None:
    print(-1)
else:
    print(index)