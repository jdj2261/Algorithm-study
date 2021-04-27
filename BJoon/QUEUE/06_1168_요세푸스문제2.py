# 못품..
from collections import deque
import sys
input = sys.stdin.readline


n, k = map(int, input().split()) 
queue = deque(i for i in range(1, n+1)) 
result = [] 

c = 0
while queue:
    queue.rotate(-k+1)
    result.append(str(queue.popleft()))

sys.stdout.write("<"+", ".join(result)+">")
