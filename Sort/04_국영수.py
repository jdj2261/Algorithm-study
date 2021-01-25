"""
Date : 20년 1월 25일
Description : Algorithm Study
Title : 국영수 (정렬) 
"""
"""
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
"""    
N = int(input())

students = []
for i in range(N):
    students.append(input().split())

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])