"""
Date : 21년 3월 26일
Description : Algorithm Study
Title : 퇴사(다이나믹 프로그래밍) 
"""
"""
입력 예시   출력 예시
7           45
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    
print(max_value)


