"""
Date : 21. 04. 28
문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.

예제 입력 1 
60466175 36
예제 출력 1 
ZZZZZ
"""

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
test = []
while n >= b:
    # n, x = divmod(n, b)
    n, x = n // b, n % b
    test.append(x)
test.append(n)
test = test[::-1]

for i in test:
    if i >= 10:
        i = i + 55
        print(chr(i), end="")
    else:
        print(i, end="")

# 다른풀이
n, p = map(int, input().split(" "))
s = ''

while(n > 0):
    n, r = divmod(n, p)
    if r > 9:
        s = chr(55+r) + s
        continue
    s = str(r) + s

print(s)