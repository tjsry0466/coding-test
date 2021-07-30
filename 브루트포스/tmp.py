n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

def go(index, first, second):



    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans


