"""
Date : 21. 04. 28

"""
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
array = list(map(int, input().split()))

result = 0
for index, data in enumerate(array):
    result += (data * (a ** (m-index-1)))

tmp = []
while result >= b:
    result, remain = divmod(result, b)
    tmp.append(remain)

tmp.append(result)

# 같은 표현
tmp.reverse()
print(*tmp)

print("%s" % (" ".join(map(str,tmp[::-1]))))
# for data in tmp[::-1]:
#     print(data, end=" ")