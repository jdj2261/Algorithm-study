"""
Date : 21년 1월 28일
Description : Algorithm Study 실전문제
Title : 고정점 찾기(이진탐색) 
"""
"""
입력 예시           출력 예시
5   
-15 -6 1 3 7        2
"""

# N = int(input())
# array = [0] * N
# list = []
# for idx, data in enumerate(input().split()):
#     array[int(idx)] = idx
#     list.append(int(data))

# result = -1
# for i in range(len(list)):
#     if list[i] == i:
#         result = i
#         break
#     else:
#         result = -1
# print(result)


# 답안지 풀이
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)





