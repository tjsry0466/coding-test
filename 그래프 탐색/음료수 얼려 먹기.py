# n x m 크기의 얼음 틀이 있다.
# 연결 된 부분끼리는 0으로 이어져 있다.
# 몇개의 아이스크림을 얼려 먹을수 있는지 구해라.

def dfs(x, y):

    if 0 <= x < n and 0 <= y < m:
        if d[x][y] == 0:
            d[x][y] = 1
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
            return True

    return False

n, m = map(int, input().split())
d = [list(map(int, input())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result +=1
print(result)