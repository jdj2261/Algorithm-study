"""
Date : 20년 12월 21일
Description : Algorithm Study
Title : Num Card Game(Greedy) 
"""

"""
N * M (행, 열)
행을 선택하여 가장 숫자가 낮은 카드 를 뽑는다.
모든 행에서 뽑은 숫자 중 가장 큰 수를 선택한다.

입력예시1       입력예시
3 3         2 4 
3 1 2       7 3 1 8
4 1 4       3 3 3 4s
2 2 2

출력예시1       출력예시2
2           3
"""

M, N = map(int, input("행 열을 입력하세요: ").split())
result = []

for i in range(M):
    data = list(map(int, input("데이터 입력 : ").split()))
    result.append(min(data))
        
print(max(result))
