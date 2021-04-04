"""
Date : 21. 04. 04
Title : 문자열 압축
"""

s = input()

result = len(s)
for step in range(1, len(s) // 2 + 1):
    prev_data = s[0:step]
    count = 1
    compressed = ""
    for i in range(step, len(s), step):
        cur_data = s[i:i+step]
        if cur_data == prev_data:
            count += 1
        else:
            compressed += str(count) + prev_data if count > 1 else prev_data
            count = 1
            prev_data = cur_data

    compressed += str(count) + prev_data if count > 1 else prev_data
    print(compressed)
    result = min(result, len(compressed))

print(result)   