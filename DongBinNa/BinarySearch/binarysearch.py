# 재귀 함수로 구현한 이진 탐색 소스코드
def recursive_binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return recursive_binary_search(array, target, start, mid-1)
    else:
        return recursive_binary_search(array, target, mid+1, end)

# 반복문으로 구현한 이진 탐색 소스코드
def loop_binary_serarch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = loop_binary_serarch(array, target, 0, n-1)
if result == None:
    print(-1)
else:
    print(result + 1)
