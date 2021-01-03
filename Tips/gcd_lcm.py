"""
최대 공약수 구하기
"""

from fractions import gcd

# 최대 공약수
print(gcd(6,8))

# 최소 공배수
def lcm(a,b):
    return  a * b // gcd(a, b)

print(lcm(6,8))