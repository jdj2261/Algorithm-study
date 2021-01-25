"""
Date : 20년 1월 25일
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
N = int(input())

score = []
for i in range(N):
    input_data = input().split()
    score.append((input_data[0], int(input_data[1])))

score = sorted(score, key=lambda student: student[1])

for student in score:
    print(student[0], end='')


