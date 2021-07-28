# 정수 n이 주어졌을때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램.
t = int(input())
ott = [1, 2, 4]
for i in range(3, 10):
    ott.append(ott[i - 3] + ott[i - 2] + ott[i - 1])
for i in range(t):
    n = int(input())
    print(ott[n - 1])

# 2번째 풀이
def go(s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s+i, goal)
    return now
t = int(input())
for _ in range(t):
    n = int(input())
    print(go(0, n))