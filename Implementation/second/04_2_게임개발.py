"""
Date : 21년 2월 19일
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

# 방문한 위치를 저장하기 위한 맵 생성 후 0으로 초기화
d = [[0]* m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)