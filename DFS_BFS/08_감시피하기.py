"""
Date : 20년 1월 19일
Description : Algorithm Study
Title : 감시 피하기
 (DFS) 
"""
"""
입력예시            출력예시
5
X S X X T           YES
T X S X X
X X X X X 
X T X X X 
X X T X X 
"""

from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
        
        if board[i][j] == 'X':
            spaces.append((i,j))

def watch(x, y , direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1

    # 오른쪽 방향으로 감시
    if direction == 1 :
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

     # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽 방향으로 감시
    if direction == 0:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
            