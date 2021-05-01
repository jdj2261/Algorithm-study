"""
Date : 21. 05. 01
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1 
3 16
예제 출력 1 
3
5
7
11
13
"""

# 에라토스테네스의 체
# 다시 풀기
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

prime = [True] * (n+1)

for i in range(2, int(n**0.5)+1):
    if prime[i] == True:
        for j in range(2*i, n+1, i):
            prime[j] = False

for i in range(m, n+1):
    if i == 1:
        continue
    if prime[i] == True:
        print(i)