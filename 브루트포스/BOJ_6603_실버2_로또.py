def go(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return
    if index == len(a):
        return

    go(a, index+1, lotto+[a[index]])
    go(a, index+1, lotto)

while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break
    go(a, 0, [])
    print()

