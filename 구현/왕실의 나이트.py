# 체스의 말이 이동할수 있는 위치의 개수가 몇개가 되는지 구하는 문제

dx = [-2, -2, -1, -1, 2, 2, 1, 1]
dy = [-1, 1, -2, 2, 1, -1, 2, -2]

c = input()
x, y = int(ord(c[0])-96), int(c[1])

ans = 0

for i in range(len(dx)):
    nx, ny = x+dx[i], y+dy[i]
    if 0 < nx <= 8 and 0 < ny <= 8:
        ans+=1

print(ans)




