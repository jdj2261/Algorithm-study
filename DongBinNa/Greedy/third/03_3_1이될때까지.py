"""
Date : 20년 3월 1일
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

n, k = map(int, input().split())

count = 0
while (n > 1):
    if n % k == 0:
        n = n//k 
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# 답안지 풀이

result = 0
while True:
    # n == k로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k
    result += (n-target)
    n = target

    # n이 k보다 작을 때 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

result += (n-1) # 남은 수에 대하여 1씩 빼기
print(result)