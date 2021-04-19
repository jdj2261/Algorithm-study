"""
Date : 21년 4월 20일
Description : Baekjoon 
Title : 카드구매하기
"""
"""
입력
첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)

둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

출력
첫째 줄에 민규가 카드 N개를 갖기 위해 지불해야 하는 금액의 최댓값을 출력한다.

예제 입력 1 
4
1 5 6 7
"""
# 다시 풀기

n = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n+1)]


for i in range(1,n+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])