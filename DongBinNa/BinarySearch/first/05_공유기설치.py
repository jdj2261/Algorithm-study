"""
Date : 21년 1월 28일
Description : Algorithm Study 실전문제
Title : 공유기 설치(이진탐색) 
"""
"""
입력 예시   출력 예시
5 3         3    
1
2
8
4
9
"""
import sys
N, C = map(int, input().split())
array = [int(sys.stdin.readline()) for _ in range(N)]
array.sort()

start = 1
end = array[-1] - array[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1

    for i in range(1,N):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)



