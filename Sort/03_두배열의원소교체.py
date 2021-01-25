"""
Date : 20년 1월 25일
Description : Algorithm Study
Title : 두 배열의 원소 교체 (정렬) 
"""
"""
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합 최댓값 출력하기
입력 예시           출력 예시
1 2 5 4 3            26
5 5 6 6 5
"""             

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break           
print(A, B)
print(sum(A))