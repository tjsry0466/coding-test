# 게임 개발
# 게임 캐릭터를 맵 안에서 움직여보면서 어디까지 움직이는지 테스트 해보는 문제
# 1. 왼쪽 방향부터 갈곳을 정한다.
# 2. 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면. 왼쪽 방향으로 회전한 다음에 왼쪽으로 한칸을 3전진한다.
#    왼쪽 방향에 가보지 않은 칸이 ㅇ벗다면, 왼쪽방향으로 히ㅗ전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸이 경우에는 바라보는 방향을 유지한채 한 칸 뒤로 가고 1단계로 돌아간다.
#    단, 이떄 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

n, m = map(int, input().split())
x, y, d = map(int,input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = [[False] * m for _ in range(n)]
check[x][y] = True
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 1

def turn_left():
    global d
    d -=1
    if d == -1:
        d = 3

turn_time = 0
while True:

    turn_left()
    nx, ny = x + dx[d], y + dy[d]

    if check[nx][ny] == False and matrix[nx][ny] == 0:
        x, y = nx, ny
        check[nx][ny] = True
        flag = True
        ans +=1
        turn_time = 0
        continue
    else:
        turn_time +=1

    if turn_time == 4:
        nx, ny = x-dx[d], y-dx[d]
        if matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0


print(ans)



