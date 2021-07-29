n = int(input())

def go(s, goal):
    if s == goal:
        return 1
    if s > goal:
        return 0
    ans = 0
    for i in range(1, 4):
        ans += go(s+i, goal)
    return ans

for i in range(n):
    k = int(input())
    print(go(0, k))