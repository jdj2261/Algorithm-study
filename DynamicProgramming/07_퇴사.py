"""
Date : 20년 1월 31일
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
t = [] # 각 상담을 완료하는 데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + 1
    # 상담이 기간 안에 끝나는 경우    
    if time <= n:
        # 점화식에 맞게, 현재까지 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)
