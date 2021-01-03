"""
Date : 21년 1월 2일
Description : 프로그래머스 문제
Title : 소수찾기(Implementation) 
address : https://programmers.co.kr/learn/courses/30/lessons/42839
"""

"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""


from itertools import permutations
import math
def solution(numbers):
    numbers = [list(permutations(numbers,i)) for i in range(1, len(numbers)+1)]

    number_list = []

    for i in numbers:
        for tmp in i:
            number_list.append(list(tmp))

    result = []
    for i in number_list:
        test = int(''.join(i))
        result.append(test)
    myset = set(result)
    result = list(myset)

    print(result)


    answer = 0
    for numbers in result:
        count = 0
        sqrt = int(math.sqrt(numbers))

        if numbers == 0 or numbers == 1 :
            continue

        for i in range(2, sqrt + 1):
            if numbers % i == 0:
                count += 1
                
        if count == 0:
            # print("소수입니다.")
            answer += 1
        # count = 0
    return answer

test = "17"
print(solution(test))
