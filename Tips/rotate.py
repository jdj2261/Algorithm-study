"""
2차원 배열을 왼쪽 or 오른쪽으로 90도 회전
"""

def rotate_left_90(arr):
    return list(zip(*arr))[::-1]

def rotate_right_90(arr):
    return list(zip(*arr[::-1]))

def rotate_a_matrix_by_90_degree(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

test_arr = [[0,0,0], [1,0,0], [0,1,1]]

print("original: {}".format(test_arr))
print("left rotate: {}".format(rotate_left_90(test_arr)))
print("right rotate: {}".format(rotate_right_90(test_arr)))
print("another right rotate: {}".format(rotate_a_matrix_by_90_degree(test_arr)))