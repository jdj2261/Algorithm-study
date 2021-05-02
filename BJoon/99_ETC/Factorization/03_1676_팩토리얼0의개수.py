"""
Date : 21. 05. 02
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1 
10
예제 출력 1 
2
예제 입력 2 
3
예제 출력 2 
0
"""
import sys
input = sys.stdin.readline

n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
array = list(map(int, str(result)))

cnt = 0
for i in range(len(array)-1, -1, -1):
    if array[i] == 0:
        cnt += 1
    else:
        break
print(cnt)
        
# 다른 풀이
N = int(input())

ans = 0
# 주어진 범위가 500이기때문에 125까지만 생각하면 된다.
for i in range(2, N + 1):
    if i % 5 == 0: ans += 1
    if i % 25 == 0: ans += 1
    if i % 125 == 0: ans += 1

print(ans)