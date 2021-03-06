"""
Date : 20년 3월 6일
Description : Algorithm Study
Title : 성적이 낮은 순서로 학생 출력하기 (정렬) 
"""
"""
성적이 낮은 순서대로 학생의 이름 출력하기
입력 예시       출력 예시              
2           이순신 홍길동
홍길동 95
이순신 77
"""  
n = int(input())

data = []
for _ in range(n):
    data.append(input().split())

array = sorted(data, key=lambda data:data[1])

for student in array:
    print(student[0], end=' ')
