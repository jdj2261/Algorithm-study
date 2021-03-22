"""
Date : 21년 3월 22일
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
# 감이 안잡히는 문제....
n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
# 1 2 4 8 9

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1

    #현재 mid값을 이용해 공유기 설치
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)