def go(index, selected):
    if index == 6:
        return

    for i in range(len(a)):
        go(index+1, selected+str(a[i]))

while True:
    a = input().split()


