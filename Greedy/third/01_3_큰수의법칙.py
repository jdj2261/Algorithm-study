"""
Date : 21년 3월 1일
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

n, m, k = map(int, input().split())
input_data = list(map(int, input().split()))

input_data.sort()

first = input_data[n-1] # 가장 큰 수
second = input_data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 (수열) 
count = m // (k+1) * k
count += m % (k+1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)