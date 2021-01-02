"""
Date : 21년 1월 1일
Description : Algorithm Study 실전문제
Title : 문자열 압축(Implementation) 
"""

"""
문제생략

입력예시                출력예시
"aabbaccc"              7
"ababcdcdababcdcd"      9
"abcabcdede"
"abcabcabcabcdedededede" 14
"xababcdcdababcdcd"     17
"""

input_str = input("문자열을 입력하세요: ")
print(input_str)

answer = len(input_str)
for i in range(1,int(len(input_str)/2)+1):
    compare_data = input_str[0:i]
    count = 1
    result = ""
    for j in range(i, len(input_str), i):
        if compare_data == input_str[j : j+i]:
            count += 1
        else:
            result += str(count) + compare_data if count >= 2 else compare_data
            compare_data = input_str[j:j+i]
            count = 1
    
    result += str(count) + compare_data if count >=2 else compare_data
    print(result)
    answer = min(answer, len(result))

print(answer)
