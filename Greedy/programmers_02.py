"""
Date : 21년 1월 4일
Description : 프로그래머스 문제
Title : 큰 수 만들기(Greedy) 
address : https://programmers.co.kr/learn/courses/30/lessons/42862
"""

"""
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841
"""

from itertools import combinations

# def solution(number, k):
#     answer = ''
#     number = list(number)
#     data_list = list(map(''.join, combinations(number,len(number) - k)))
#     answer = str(max(data_list))
#     return answer

# print(solution("1924", 2))
# 실패..
def solution(number, k):
    st = []

    for elem in number:
        while st and st[-1] < elem and k > 0:
            st.pop()
            k -= 1

        st.append(elem)

    while k > 0:
        st.pop()
        k-=1

    answer = "".join(st)
    return answer

def solution2(number, k):
    collected = []

    for (i, num) in enumerate(number):
        print(collected)
        while collected and collected[-1] < num and k > 0:
            print(i, collected[-1])
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

def solution3(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

print(solution2("1923",2))
# number = "4177252841"
# number = list(number)
# k = 4

# result = []
# while(k!=0):
#     for i in range(len(number)-1):
#         if number[i] < number[i+1]:
#             print(i)
#             k -= 1
#             result.append(number[i])
# print(result)