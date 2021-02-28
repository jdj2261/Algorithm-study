"""
Date : 21년 2월 14일
Description : Algorithm Study
Title : 숫자 카드 게임 (Greedy) 
"""
"""
N * M (행, 열)
행을 선택하여 가장 숫자가 낮은 카드 를 뽑는다.
모든 행에서 뽑은 숫자 중 가장 큰 수를 선택한다.

입력예시1     입력예시
3 3         2 4 
3 1 2       7 3 1 8
4 1 4       3 3 3 4
2 2 2

출력예시1     출력예시2
2           3
"""

n, m = map(int, input().split())

result = []

for _ in range(n):
    result.append(min(list(map(int, input().split()))))

print(max(result))