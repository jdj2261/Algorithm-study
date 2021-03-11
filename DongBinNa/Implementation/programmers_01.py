"""
Date : 21년 1월 2일
Description : 프로그래머스 문제
Title : 모의고사(Implementation) 
address : https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
"""

"""
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.
"""

# import copy


def solution(answers):
    
    answer = []

    first_student = [1,2,3,4,5]
    second_student = [2,1,2,3,2,4,2,5]
    third_student = [3,3,1,1,2,2,4,4,5,5]

    len_answers = len(answers)

    len_first_student = len(first_student)

    share = len_answers // len_first_student
    remainder = len_answers % len_first_student

    if len_answers > len_first_student:
        result_first = first_student * share
        result_second = second_student * share
        result_third = third_student * share
        if remainder != 0:
            for i in range(remainder):
                result_first.append(first_student[i])
                result_second.append(second_student[i])
                result_third.append(third_student[i])
    else:
        result_first = []
        result_second = []
        result_third = []
        for i in range(len_answers):
            result_first.append(first_student[i])
            result_second.append(second_student[i])
            result_third.append(third_student[i])

    first_result = []
    second_result = []
    third_result = []
    for i in range(len_answers):
        if result_first[i] == answers[i]:
            first_result.append(result_first[i])
        if result_second[i] == answers[i]:
            second_result.append(result_second[i])
        if result_third[i] == answers[i]:
            third_result.append(result_third[i])

    result = []
    result.append(len(first_result))
    result.append(len(second_result))
    result.append(len(third_result))

    for person, score in enumerate(result):
        if score == max(result):
            answer.append(person+1)

    return answer

# 깔끔한 풀이
def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# itertools 이용
from itertools import cycle

def solution3(answers):
    pl_1 = [1,2,3,4,5]
    pl_2 = [2,1,2,3,2,4,2,5]
    pl_3 = [3,3,1,1,2,2,4,4,5,5]
    scores=[0,0,0]
    winner=[]

    for i, j, k, ans in zip(cycle(pl_1), cycle(pl_2), cycle(pl_3), answers) :
        if i==ans:  scores[0]+=1
        if j==ans:  scores[1]+=1
        if k==ans:  scores[2]+=1
    
    for index, score in enumerate(scores):
        if score == max(scores):
            winner.append(index+1)
    winner.sort()

    return winner

print(solution3([1,2,3,4,5]))