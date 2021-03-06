"""
Date : 21년 3월 6일
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
origin_data = list(map(int, input().split()))
origin_data.sort()
m = int(input())
compare_data = list(map(int, input().split()))

for target in compare_data:
    result = binary_search(origin_data, target, 0, n-1)
    if result != None:
        print('yes', end =' ')
    else:
        print('no', end=' ')
print()

# 계수 정렬 풀이
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

# set
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')