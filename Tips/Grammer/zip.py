"""
zip 사용하기
"""

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

result = zip(number_list, str_list)

# Converting iterator to set
# list : 순서 O
# set  : 순서 X 
result_list = list(result)
print(result_list)

# result_set = set(result)
# print(result_set)

# unzip
number, str_data = zip(*result_list[::-1])
print('number: {}'.format(number))
print('str_data: {}'.format(str_data))

rotate_list = list(zip(*result_list[::-1]))
print("rotate: {}".format(rotate_list))