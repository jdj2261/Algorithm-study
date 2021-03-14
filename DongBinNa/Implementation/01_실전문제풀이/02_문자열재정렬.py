"""
Date : 21년 3월 15일
Description : Algorithm Study 실전문제
Title : 문자열 재정렬(Implementation) 
"""

"""
문제 생략

입력예시            출력예시
K1KA5CB7        ABCKK13

입력예시                출력예시
AJKDLSI412K4JSJPD   ADDIJJJKKLSS20
"""

datas = list(input())

alpha_list, digit_list = [], []

for data in datas:
    if data.isalpha():
        alpha_list.append(data)
    else:
        digit_list.append(int(data))
alpha_list.sort()
result = ''.join(alpha_list) + str(sum(digit_list))
print(result)