"""
Date : 21. 05. 02
문제
끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n, m (0 <= m <= n <= 2000000000, n!= 0)이 들어온다.

출력
첫째 줄에 끝자리 0의 개수를 출력한다.

예제 입력 1 
25 12
예제 출력 1 
2
"""
# 다시 풀기
import sys
n, m = map(int, sys.stdin.readline().split())

def five_count(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt

def two_count(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt

if m == 0:
    print(0)  
else:       
    print(min(two_count(n)-two_count(m)-two_count(n-m), five_count(n)-five_count(m)-five_count(n-m)))

# 다른 풀이
def calx(n, x):
	s = 0
	while n:
		n //= x
		s += n
	return s
def cal0(n, m):
	f = calx(n, 5)-calx(m, 5)-calx(n-m, 5)
	t = calx(n, 2)-calx(m, 2)-calx(n-m, 2)
	return min(f, t)
n, m = map(int, input().split())
print(cal0(n, m))


# def NChooseK_fast(a, b):
#     numerator = 1
#     denominator = 1
#     b = min(a-b, b) 
#     for i in range(1, b+1):
#         denominator *= i
#         numerator *= a+1-i
#     return numerator//denominator

# result = NChooseK_fast(n, m)
# array = list(map(int, str(result)))

# cnt = 0
# for i in range(len(array)-1, -1, -1):
#     if array[i] == 0:
#         cnt += 1
#     else:
#         break
# print(cnt)


# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n+1):
#             result *= i
#     return result

# def cal_combination(a, b):
#     return factorial(a) // (factorial(b) * factorial(a-b))