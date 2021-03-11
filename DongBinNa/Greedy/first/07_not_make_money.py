"""
Date : 20년 12월 22일
Description : Algorithm Study 실전문제풀이 4
Title : 만들 수 없는 금액(Greedy) 
"""

"""
N개의 동전을 이용하여 만들 수 없는 양의 점수 금액 중 최솟값 구하기

입력 예시       출력예시
3 2 1 1 9       8
"""

money = list(map(int, input("숫자를 입력하세요: ").split()))
money.sort()
print(money)

make_money = 0
result = 0

if money[0] == 1:
    for i in range(len(money)-1):
        make_money += money[i]
        if money[i+1] - make_money >= 2:
            result = make_money + 1 
            break
        else:
            result = make_money + money[-1]+ 1
else:
    result = 1

print(result)

# 답안지 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)