"""
Date : 21. 04. 28
문제
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

입력
첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.

예제 입력 1 
11001100
예제 출력 1 
314
"""

import sys
input = sys.stdin.readline

n = input().strip()
step = -3
result = ""
for i in range(len(n), -1, step):
    start = i+step
    if start < 0:
        start = 0
    data = n[start:i]
    if data :
        result += str(int(data, 2))
print(result[::-1])

# 다른 풀이
print(format(int(input(), 2), 'o'))