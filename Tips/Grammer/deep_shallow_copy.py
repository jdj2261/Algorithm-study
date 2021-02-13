import copy

# 얕은 복사
a = [1, [1, 2, 3]]
b = copy.copy(a)
print("="*40)
print("Shallow Copy example")
print("Origin list a : {}".format(a))
print("Before list b : {}".format(b))
b[0] = 100
print("After list b : {}".format(b))
print("After list a : {}".format(a))

c = copy.copy(a)
c[1].append(4)
print("After list c : {}".format(c))
print("After list a : {}".format(a))
print("="*40)

a = [1, [1, 2, 3]]
b = copy.deepcopy(a)
print("="*40)
print("Deep Copy example")
b[0] = 100
b[1].append(4)
print("After list b : {}".format(b))
print("After list a : {}".format(a))
print("="*40)