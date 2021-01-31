"""
3 4       
1 3 3 2 2 1 4 1 0 6 4 7
"""
n,m = map(int,input().split())
array = list(map(int, input().split()))

dp = []
index = 0
for i in range(n):
    dp.append(array[index:index + m])
    index += m
print(dp)