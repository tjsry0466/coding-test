n, m = map(int, input().split())
alpha = input().split()
alpha.sort()

def check(password):
    mo = 0
    ja = 0
    for i in password:
        if i in 'aeiou':
            mo +=1
        else:
            ja +=1
    return ja >= 2 and mo >= 1

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return

    if i == len(alpha):
        return

    go(n, alpha, password+alpha[i], i+1)
    go(n, alpha, password, i+1)

go(n, alpha, "", 0)