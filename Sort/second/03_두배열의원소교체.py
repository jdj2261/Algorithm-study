"""
Date : 20년 3월 6일
Description : Algorithm Study
Title : 두 배열의 원소 교체 (정렬) 
"""
"""
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합 최댓값 출력하기
입력 예시           출력 예시
5 3
1 2 5 4 3            26
5 5 6 6 5
"""          
n, k = map(int, input().split())

first_data = list(map(int, input().split()))
second_data = list(map(int, input().split()))

first_data.sort()
second_data.sort(reverse=True)

for i in range(k):
    if first_data[i] < second_data[i]:
        first_data[i], second_data[i] = second_data[i], first_data[i]
    else:
        break

print(sum(first_data))

