
# 최대 공약수
a, b = map(int, input().split())

# def gcd(a, b):
#     min = a if a < b else b
#     for i in range(min+1, 1, -1):
#         if a % i == 0 and b % i == 0:
#             res = i
#             break
#     return res

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# 최소 공배수
def lcm(a,b):
    return  a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))