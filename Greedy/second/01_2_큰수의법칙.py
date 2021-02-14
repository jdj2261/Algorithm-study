"""
Date : 21년 2월 14일
Description : Algorithm Study
Title : 큰 수의 법칙 (Greedy) 
"""

"""
첫째줄 : N, M, K 자연수
둘째줄 : N개의 자연수

주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음.

입력예시
5 8 3
2 4 5 4 6

출력예시
46
"""

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

input_data = list(map(int, input().split()))
input_data.sort(reverse=True)

result = (input_data[0] * (k-1) + input_data[1]) * (m//k) + input_data[0]*(m%k)
print(result)