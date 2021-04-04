"""
Date : 21년 4월 4일
Description : Algorithm Study 실전문제
Title : 부품찾기(이진탐색) 
"""
"""
부품이 있는지 확인
입력 예시           출력예시
5               no yes yes
8 3 7 9 2
3
5 7 9
"""

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
menu = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

for target in search:
    result = binary_search(menu, target, 0, n-1)
    if result is not None:
        print("yes", end=" ")
    else:
        print("no", end=" ")


