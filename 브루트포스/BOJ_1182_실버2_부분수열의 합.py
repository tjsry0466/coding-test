n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
def go(index, sum):
    global ans
    if index == n:
        if sum == m:
            ans +=1
        return
    go(index+1, sum+a[index])
    go(index+1, sum)
go(0,0)
if m == 0:
    ans -=1
print(ans)