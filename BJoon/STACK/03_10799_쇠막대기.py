"""
Date : 21. 04. 25
문제 생략 (boj.kr/10799)
"""

# 다시 풀기
import sys
input = sys.stdin.readline

result = 0
stack = []
stick = list(input().strip())
for index in range(len(stick)):
    if stick[index] == '(':
        stack.append('(')
    else:
        if stick[index-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)