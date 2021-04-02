datas = list(map(int, input()))

zero2one = 0
one2zero = 0

compare_data = datas[0]
if compare_data == 0:
    one2zero += 1
else:
    zero2one += 1
    
for i in range(1, len(datas)):
    if compare_data != datas[i]:
        if compare_data == 0:
            zero2one += 1
        else:
            one2zero += 1
    compare_data = datas[i]


print(min(zero2one, one2zero))
