# 미로 탈출
# 최소 횟수 구하기

from collections import deque
n, m = map(int, input().split())
d = [list(map(int, input())) for _ in range(n)]
q = deque()
dist = [[-1] * (m+1) for _ in range(n+1)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

q.append((1, 1))
dist[1][1] = 1
check = [[False] * (m+1) for _ in range(n+1)]

while q:
    x, y = q.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 < nx <= n and 0 < ny <= m:
            if check[nx][ny] == False and d[nx-1][ny-1] == 1:
                check[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

print(dist[n][m])


