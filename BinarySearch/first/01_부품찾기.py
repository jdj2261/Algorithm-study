"""
Date : 21년 1월 27일
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
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

N = int(input())
array = list(map(int, input().split()))
M = int(input())
find_data = list(map(int, input().split()))

array.sort()

for i in find_data:
    result = binary_search(array, i, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
print()

# 다른 방법 (계수 정렬)
n = int(input())
array = [0] * 1000000

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 다른 방법
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
