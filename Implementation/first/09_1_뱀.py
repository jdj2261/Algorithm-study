"""
Date : 21년 2월 23일
Description : Algorithm Study 실전문제
Title : 뱀(Implementation) 
"""

"""
첫째 줄에 보드의 크기 N이 주어짐 (2~100)
다음 줄에는 K (0~100)
다음 K 줄에는 사과의 위치 (행, 열)
다음 줄에는 뱀의 방향 변환 횟수 L(1~100)
다음 L개의 줄 (X, C) X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로 90도 회전
게임이 몇 초에 끝나는 것인가?

"""

def rotation(c):
    global heading
    if c == 'L':
        heading -= 1
    else:
        heading += 1
    
    if heading < 0:
        heading = 3
    elif heading > 3:
        heading = 0

N = int(input())
K = int(input())

board = [[0] * (N+1) for _ in range(N + 1)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1


x, y, heading = 1, 1, 1
time = 0
board[x][y] = 2
index = 0
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

L = int(input())

changes = []
for _ in range(L):
    X, C = input().split()
    changes.append((int(X), C))

# 뱀 현재 위치 저장
snake = [(x, y)]

while True:
    nx = x + dx[heading]
    ny = y + dy[heading]

    if 1 <= nx and nx <= N and 1 <= ny and ny <= N and board[nx][ny] != 2:

        # 사과를 먹는 경우
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            snake.append((nx, ny))
        else:
            board[nx][ny] = 2
            snake.append((nx, ny))
            px, py = snake.pop(0)
            board[px][py] = 0

    else:
        time += 1
        break
    x, y = nx, ny
    time += 1
    # 방향이 바뀌는 경우
    if  index < L and time == changes[index][0]:
        print(time, "rotate")
        rotation(changes[index][1])
        index += 1

print(time)









