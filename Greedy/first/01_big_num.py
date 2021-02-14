"""
Date : 20년 12월 21일
Description : Algorithm Study
Title : Big Num (Greedy) 
"""

"""
첫째줄 : N, M, K 자연수
둘째줄 : N개의 자연수

주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음.

입력예시
5 8 3
2 4 5 4 6

출력예시
46
"""

N, M, K = map(int, input("N, M, K 입력").split())
print("N : {}, M :{}, K : {}".format(N,M,K))
test = list(map(int, input("숫자 입력").split()))
test.sort()

first_num = test[N-1]
second_num = test[N-2]

result = 0

# 풀이 1
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += first_num
#         M -= 1
 
#     if M == 0:
#         break
#     result += second_num
#     M -= 1

# print(result)

# 풀이 2
count = int(M / (K+1)) * K
count += M % (K+1)

result = 0
result += (count) * first_num
result += ( M - count) * second_num

print(result)