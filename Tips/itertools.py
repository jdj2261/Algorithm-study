import itertools
from itertools import permutations  # 순열
from itertools import combinations  # 조합
from itertools import product       # 중복순열
from itertools import chain         # 2차배열 -> 1차배열


print(list(permutations(range(1, 5), 3)))

print(list(combinations('ABC', 2)))

# 문자열로 합치기
number = "1234"
data_list = list(map(''.join, combinations(number,2)))
print(data_list)

# product(range(1,n1+1), range(1,n2+1), range(1,n3+1))

or_not = [(0, 500), (0, 1500)]

print(list(product(*or_not)))

print(list(chain(*or_not)))