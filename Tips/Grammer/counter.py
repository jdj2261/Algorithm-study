import collections
my_list = ["a", "a", "b", "b", "c"]
test = collections.Counter(my_list)
print(test)


# keys 이용
for key in test:
    print(key)

# items 이용
for key, value in test.items():
    print(key, value)

