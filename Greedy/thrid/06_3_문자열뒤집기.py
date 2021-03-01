"""
Date : 21년 3월 1일
Description : Algorithm Study 실전문제풀이 2
Title : 문자열 뒤집기(Greedy) 
"""

"""
0과 1로만 이루어진 문자열 S
연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이고, 모두 같은 숫자로 만들기 위한 최소 횟수 구하기

입력예시    출력예시
0001100     1
"""

# 첫번째 문자열과 비교 후 뒤집어진 개수 중 최소를 선택하는데..
# 첫번째 인덱스의 값도 신경을 써줘야 된다!

input_list = list(map(int, input()))

zero2one_cnt = 0
one2zero_cnt = 0

compare_data = input_list[0]

if compare_data == 1:
    zero2one_cnt +=1 
else:
    one2zero_cnt += 1

for i in range(1, len(input_list)):
    if input_list[i] != compare_data:
        if input_list[i] == 0:
            one2zero_cnt += 1
        else:
            zero2one_cnt += 1
        compare_data = input_list[i]

# print(zero2one_cnt, one2zero_cnt)
print(min(zero2one_cnt, one2zero_cnt))

