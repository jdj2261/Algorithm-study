"""
Date : 20년 12월 21일
Description : Algorithm Study
Title : Chage (Greedy) 
"""

"""
거스름돈을 500, 100, 50, 10원 짜리로 준다고 했을 때, 거슬러줘야 할 동전의 최소 개수는?
동전의 개수는 무한히 존재하며, 거슬러 줘야 할 돈 N은 항상 10의 배수
"""

# 2660 = 500 * 5 + 100 * 1 + 50 * 1 + 10 * 1 
# Answer = 8

input_money = int(input("거스름돈을 입력하세요 : "))
count = 0

list = [500, 100, 50, 10]

for coin in list:
    count += input_money // coin
    input_money %= coin

print(count)