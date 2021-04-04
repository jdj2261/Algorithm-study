s = input()

result = len(s)
for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev_data = s[0:step]
    count = 1
    for i in range(step,len(s),step):
        if s[i:i+step] == prev_data:
            count += 1
        else:
            compressed += str(count) + prev_data if count > 1 else prev_data
            prev_data = s[i:i+step]        
            count = 1
    compressed += str(count) + prev_data if count > 1 else prev_data
    result = min(result, len(compressed))
print(result)
