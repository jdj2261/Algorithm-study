# for i in range(1, int(input())+1):
#     print('*'*i)

# n = int(input())
# for i in range(1, n + 1):
#     print(" "*(n-i)+"*"*i)

# n = int(input())
# for i in range(n, 0, -1):
#     print("*"*i)

# n = int(input())
# for i in range(n, 0, -1):
#     print(" "*(n-i)+ "*"*i)

# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))

# n = int(input())
# for i in range(1, 2*n):
#     if i <= n:
#         print("*"*i + " "*(2*(n-i)) + "*"*i)
#     else:
#         print("*"*(2*n-i)+" "*(2*(i-n))+"*"*(2*n-i))

# n = int(input())
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*i)
# for i in range(n-1, 0, -1):
#     print(" "*(n-i)+"*"*i)
    
n = int(input())
for i in range(n, 0, -1):
    print(" "*(n-i)+"*"*(2*i-1)+" "*(n-i))
for i in range(1, n):
    print(" "*(n-1-i)+"*"*(2*i+1)+" "*(n-1-i))