"""
Date : 20년 2월 14일
Description : Algorithm Study
Title : 1이 될 때까지(Greedy) 
"""

"""
N이 1이 될 때 까지
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수 구하기

입력 예시
25 5

출력 예시
2
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = 0
while (n != 1):
    if n >= k:
        n //= k 
        result += 1
    else:
        n -= 1
        result += 1
print(result)