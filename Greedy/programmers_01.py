"""
Date : 21년 1월 3일
Description : 프로그래머스 문제
Title : 체육복(Implementation) 
address : https://programmers.co.kr/learn/courses/30/lessons/42862
"""

"""
문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
입출력 예 설명
예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
"""
from itertools import combinations

# n = 3
# lost = [3]
# reserve = [1]

# answer = n - len(lost) # 3

# test = lost + reserve
# test = [ i for i in combinations(test,2) if i not in combinations(lost,2)]
# # print(test)

# count = 0
# tmp = []
# for a,b in test:
#     if abs(a-b) <2:
#         print(a,b)
#         tmp.append(a)
#         count += 1

# tmp = set(tmp)
# tmp = list(tmp)
# # print(tmp)

# if count > len(tmp):
#     count = count - len(tmp)

# # print(count)
# if count > len(reserve):
#     count = len(reserve)
# # print(count)

# answer = answer + count
# print(answer)
# # print(test)

def solution(n, lost, reserve):
    answer = n - len(lost)
    sum_data = lost + reserve
    sum_data = [ i for i in combinations(sum_data,2) if i not in combinations(lost,2)]

    count = 0
    tmp_count = 0
    tmp_a = []
    tmp_b = []
    for a,b in sum_data:
        if abs(a-b) <2:
            print(a,b)
            tmp_a.append(a)
            tmp_b.append(b)
            tmp_count += 1


    tmp_a = set(tmp_a)
    tmp_a = list(tmp_a)

    tmp_b = set(tmp_b)
    tmp_b = list(tmp_b)
    print(tmp_a, tmp_b)

    if len(tmp_a) > len(tmp_b):
        count = len(tmp_b)
    elif len(tmp_a) < len(tmp_b):
        count = len(tmp_a)
    else:
         count = tmp_count
    # tmp = set(tmp)
    # tmp = list(tmp)
    
    # print(tmp)

    # print(count)

    if count > len(reserve):
        count = len(reserve)

    answer = answer + count
    return answer

print(solution(10, [1,3,4,5,7,10], [2,6,8]))
print(solution(5, [2,4], [1,3,5]))