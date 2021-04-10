# 내풀이
data = input()
n = len(data)
for i in range(0, n, 10):
    if n > 10:
        print(data[i:i+10])
        n -= 10
    else:
        print(data[i:i+n])

# 이렇게 풀자..
a = input()
for i in range(0,len(a),10):
    print(a[i:i+10])