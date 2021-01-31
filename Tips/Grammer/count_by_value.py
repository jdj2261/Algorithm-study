from bisect import bisect_left, bisect_right
def count_by_value(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

array = [1,2,2,3,4]

count = count_by_value(array, 2, 2)
print(count)