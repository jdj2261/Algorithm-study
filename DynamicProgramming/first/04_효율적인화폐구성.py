"""
Date : 21년 1월 31일
Description : Algorithm Study
Title : 효율적인 화폐 구성(다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
2 15        5
2
3
"""
N, M = map(int, input())
array = [int(input()) for _ in range(N)]

d = [10001] * (M+1)

d[0] = 0                                     
for i in range(N):
    for j in range(array[i], M+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j- array[i] + 1])
        
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
