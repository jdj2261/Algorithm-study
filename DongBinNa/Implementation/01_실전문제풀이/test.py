s = input()
answer = len(s)
for step in range(1, len(s) //2 + 1):
    compare_data = s[0:step]
    count = 1
    compressed = ""
    for data in range(step, len(s), step):
        if compare_data == s[data:data+step]:
            count += 1
        else:
            compressed += str(count) + compare_data if count >= 2 else compare_data
            compare_data = s[data : data+step]
            count = 1
    compressed += str(count) + compare_data if count >= 2 else compare_data
    answer = min(answer, len(compressed))

print(answer)
    