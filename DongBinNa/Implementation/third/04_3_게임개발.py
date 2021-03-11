"""
Date : 21년 3월 1일
Description : Algorithm Study 실전문제
Title : 게임 개발(Implementation) 
"""

"""
문제 생략

입력예시
4 4         # 4 x 4 맵 생성
1 1 0       # (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
1 1 1 1     # 첫 줄은 모두 바다
1 0 0 1     # 둘째 줄은 바다/육지/육지/바다
1 1 0 1     # 셋째 줄은 바다/바다/육지/바다
1 1 1 1     # 넷째 줄은 모두 바다

출력 예시
3
"""

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# d = [0, 1, 2, 3]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 위치 저장
data = [ [0] * m for _ in range(n)]
data[x][y] = 1

def turn_left():
    global direction
    direction = direction - 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if data[nx][ny] == 0 and graph[nx][ny] == 0:
        data[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(cnt)