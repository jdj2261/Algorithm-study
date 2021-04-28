"""
Date : 21. 04. 27
"""

import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b // gcd(a,b)

for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a,b))
