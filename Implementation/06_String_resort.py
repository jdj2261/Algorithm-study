"""
Date : 21년 1월 1일
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

datas = input("문자와 숫자를 연속해서 입력하세요: ")

char_list = []
digit_list = []
sum = 0
for data in datas:
    if data.isdigit():
        sum += int(data)
    else:
        char_list.append(data)

char_list.sort()
char_list.append(str(sum))

print(''.join(char_list))
