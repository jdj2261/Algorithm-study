"""
for 문과 재귀함수 비교
팩토리얼 계산
"""
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    # 종료 조건 꼭 넣어야 함.
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print("반복적으로 구현 :{}".format(factorial_iterative(5)))
print("재귀적으로 구현 :{}".format(factorial_recursive(5)))