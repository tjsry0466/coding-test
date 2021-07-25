n = int(input())
m = int(input())
if m:
    arr = set(input().split())
else:
    arr = set()

ans = abs(n - 100)

for num in range(1000001):
    for n in str(num):
        if n in arr:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - ans))

print(ans)



