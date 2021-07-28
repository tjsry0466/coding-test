# 순서로 푸는 방법 (2를 활용)
n, m = map(int, input().split())
a = [0] * (m)
def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    for i in range(start, n+1):
        a[index] = i
        go(index+1, i, n, m)

go(0, 1, n, m)

# 선택으로 푸는 방법 (틀림,,)
import sys
n,m = map(int,input().split())
a = [0]*m
def go(index, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    if index > n:
        return

    for i in range(m-selected, 0, -1):
        # 선택
        a[index] = i
        go(index+1, selected+i, n, m)
    # 선택 x
    a[index] = 0 # 있어도 되고 없어도 되는 부분
    go(index+1, selected, n, m)

go(1,0,n,m)