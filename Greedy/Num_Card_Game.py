n, m = map(int, input().split())

result = 0 
result_list = []
for i in range(n):
    current_line = list(map(int, input().split()))
    print(current_line)
    min_value = min(current_line)
    result = max(result, min_value)

print(result)