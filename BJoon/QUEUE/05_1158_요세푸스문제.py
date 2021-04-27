"""
Date : 21. 04. 26

문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

출력
예제와 같이 요세푸스 순열을 출력한다.

예제 입력 1 
7 3
예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
"""
# 바로 맞춤
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))
stack = []

cnt = 0
while queue:
    cnt += 1
    num = queue.popleft()
    if cnt != k :
        queue.append(num)
    else:
        stack.append(num)
        cnt = 0

print("<%s>" % (", ".join(map(str,stack))))

# # 다른풀이
# #[BOJ] 백준 파이썬 > 1158번 요세푸스 문제 
# n, k = map(int,input().split()) 
# nl = [i for i in range(1,n+1)] 
# answer = [] 
# num = 0 
# while len(answer) != n: 
#     num = (num + (k-1)) % len(nl) 
#     answer.append(nl.pop(num)) 
# print("<%s>" % (", ".join(map(str,answer))))

# # 다른풀이
# n, k = map(int, input().split()) 
# q = [] 
# result = [] 

# for i in range(n): 
#     q.append(i+1) 
#     c = 0 
    
# while len(q) >0:
#     c = (c + (k-1)) % len(q)
#     cc = q.pop(c) 
#     result.append(str(cc))

# print("<%s>" %(", ".join(result)))