"""
Date : 21. 04. 04
Title : 모험가 길드
"""

n = int(input())
array = list(map(int, input().split()))
array.sort()

count = 0
result = 0
for i in array:
    count += 1
    if count >= i:
        result = max(result, count)
        count = 0

print(result)


