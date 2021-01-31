"""
Date : 20년 1월 31일
Description : Algorithm Study
Title : 금광(다이나믹 프로그래밍) 
"""
"""
입력 예시                               출력 예시
2                                       19
3 4                                     16
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

for tc in range(int(input())):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m
    print(dp)
    for j in range(1, m):
        for i in range(n):
            if i == 0 :
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)
