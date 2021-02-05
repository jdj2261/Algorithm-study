"""
Date : 20년 2월 4일
Description : Algorithm Study
Title : 편집거리(다이나믹 프로그래밍) 
"""
"""
입력 예시    출력 예시
cat         1
cut

sunday      3
saturday
"""

def edit_dis(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dis(str1,str2))

