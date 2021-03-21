"""
Date : 21년 1월 26일
Description : Algorithm Study 실전문제
Title : 실패율(정렬) 
"""

"""
입력 예시               출력 예시
5                   [3, 4, 2, 1, 5]
2 1 2 6 2 4 3 3
"""

N = int(input())

# stages = list(map(int, input().split()))
stages = [2,1,2,6,2,4,3,3]
# stages = [4, 4, 4, 4]
len_stages = len(stages)
stages.sort()

fail_list = []
fail_rate = 0
for i in range(1, N+1):
    fail_rate = stages.count(i)/len_stages
    fail_list.append((i, fail_rate))
    len_stages = len_stages - stages.count(i)

answer = sorted(fail_list, key=lambda t : t[1], reverse=True)
answer = [i[0] for i in answer]
print(answer)
