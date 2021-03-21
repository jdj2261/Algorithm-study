"""
Date : 21년 3월 21일
Description : Algorithm Study
Title : 국영수 (정렬) 
"""
"""
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
"""   
n = int(input())
array = []

for _ in range(n):
    array.append(list(input().split()))

array.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in array:
    print(i[0])