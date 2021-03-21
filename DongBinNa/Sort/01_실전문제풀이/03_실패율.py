"""
Date : 21년 3월 22일
Description : Algorithm Study 실전문제
Title : 실패율(정렬) 
"""

"""
입력 예시               출력 예시
5                   [3, 4, 2, 1, 5]
2 1 2 6 2 4 3 3
"""

n = int(input())

stages = list(map(int, input().split()))
length = len(stages)
answer = []
for i in range(1, n+1):
    count = stages.count(i)

    if length == 0:
        fail = 0
    else:
        fail = count /length
    
    answer.append((i, fail))
    length -= count

answer = sorted(answer, key=lambda x: x[1], reverse=True)
answer = [i[0] for i in answer]
print(answer)
    