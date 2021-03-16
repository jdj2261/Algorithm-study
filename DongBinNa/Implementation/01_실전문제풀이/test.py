datas = input()
answer = len(datas)
for step in range(1, len(datas) // 2 + 1):
    compressed = ""
    prev = datas[0:step]
    count = 1
    for j in range(step, len(datas), step):
        if prev == datas[j: j + step]:
            count += 1
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = datas[j : j + step]
            count = 1
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))

print(answer)
    
