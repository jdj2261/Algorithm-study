"""
Date : 20년 12월 31일
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

N, M = map(int, input("세로와 가로 크기를 입력하세요: ").split())
x, y, direction = map(int, input("현재 좌표와 방향을 입력하세요: ").split())
map_datas = []

for i in range(M):
    map_datas.append(list(map(int,input("바다 또는 육지를 입력하세요:").split())))
print(map_datas)

isVisit = [[0] * M for _ in range(N)]
isVisit[x][y] = 1
# print(isVisit)
count = 1
turn_time = 0

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3 

# 처음 단계
while True:

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if isVisit[nx][ny] == 0 and map_datas[nx][ny] == 0:
        isVisit[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        count += 1
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if map_datas[nx][ny] == 0:
            x = nx
            y = nx
        else:
            break
        turn_time = 0
# result = isVisit.count(True)
print(count)

