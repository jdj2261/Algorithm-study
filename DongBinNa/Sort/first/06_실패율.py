"""
Date : 21년 1월 26일
Description : Algorithm Study 실전문제
Title : 실패율(정렬) 
"""

"""
모든 집까지의 거리의 총합이 최소가 되도록 안테니 설치
입력 예시    출력 예시
4             5
5 1 7 9
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
