"""
Date : 20년 12월 21일
Description : Algorithm Study
Title : Remain 1(Greedy) 
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

N, K = map(int, input("N과 K를 입력하세요: ").split())

result = 0
while(N != 1):
    if (N % K != 0):
        N -= 1
        result += 1
    else:
        N /= K
        result += 1
    
print(result)