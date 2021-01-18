# 중복 순열
from itertools import product

n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n-1))))