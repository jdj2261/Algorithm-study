"""
Date : 21. 05. 01
문제
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

입력
입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 
만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다. 
또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

예제 입력 1 
8
20
42
0
예제 출력 1 
8 = 3 + 5
20 = 3 + 17
42 = 5 + 37
"""
import sys
input = sys.stdin.readline

def find_prime(n: int) -> list:
    prime = [True] * (n+1)
    result = []
    for i in range(2, int(n**0.5) + 1):
        if prime[i] == True:
            for j in range(2*i, n+1, i):
                prime[j] = False
    for i in range(3, n+1):
        if prime[i] == True:
            result.append(i)
    return result

def sum_of_primes(n: int) -> list:
    primes = find_prime(n)
    result = []
    for i in range(len(primes) // 2):
        if n - primes[i] in primes:
            result.append((primes[i], n-primes[i]))
            break
    return result

def find_max_diff(array: list) -> tuple:
    return array[0]

while True:
    n = int(input())
    
    # 입력의 마지막 줄
    if n == 0:
        break
        
    primes = sum_of_primes(n)
    # print(primes)
    if primes:
        a, b = find_max_diff(primes)
        print(f"{n} = {a} + {b}")
    else:
        # 소수의 합으로 나타낼 수 없는 경우
        print("Goldbach's conjecture is wrong.")

# 투 포인터로 풀어야 통과..
import sys

def Goldbach():
    check = [False, False] + [True] * 1000000
    
    for i in range(2, 1001):
        if check[i] == True:
            for j in range(i + i, 1000001, i):
                check[j] = False

    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break

        A = 0
        B = n
        for _ in range(1000000):
            if check[A] and check[B]:
                print(f"{n} = {A} + {B}")
                break
            A += 1
            B -= 1
        else:
            print("Goldbach's conjecture is wrong.")

Goldbach()