"""
Date : 21년 3월 7일
Description : Algorithm Study
Title : 1로 만들기 (다이나믹 프로그래밍) 
"""
"""
X가 5로 나누어 떨어지면 5로나눈다.
3으로 나누어 떨어지면 3으로 나누고
2로 나누어 떨어지면 2로 나눈다.
X에서 1을 뺀다.
연산을 사용하는 최소 횟수는?
입력예시    출력예시
26          3
"""
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 5 == 0:
        d[i] = min(d[i], d[ i//5 ] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[x])
    