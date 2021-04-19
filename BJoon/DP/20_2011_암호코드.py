"""
Date : 21년 4월 20일
Description : Baekjoon 
Title : 암호코드
"""
"""
입력
첫째 줄에 5000자리 이하의 암호가 주어진다. 암호는 숫자로 이루어져 있다.

출력
나올 수 있는 해석의 가짓수를 구하시오. 정답이 매우 클 수 있으므로, 1000000으로 나눈 나머지를 출력한다.

암호가 잘못되어 암호를 해석할 수 없는 경우에는 0을 출력한다.

예제 입력 1 
25114
예제 출력 1 
6
"""

# 다시 풀기

import sys
n = sys.stdin.readline().strip()
if n[0] == '0':
    print('0')
    exit()

result = [1, 1]
mod = 1000000

for i in range(1, len(n)):
    cnt = 0
    num = int(n[i-1:i+1])

    if int(n[i]) > 0:
        cnt += result[-1]
    if num >= 10 and num <= 26:
        cnt += result[-2]
    result.append(cnt%mod)
print(str(result[-1]))