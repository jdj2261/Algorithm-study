n, k = map(int, input().split())
target = 0
result = 0

while True:
    target = n // k * k
    result += n - target

    n = target 
    print("result : {}, n : {}".format(result, n))
    if n < k :
        break
    result = result + 1
    # print(result)
    n //= k



result += (n-1)
print(result)
    