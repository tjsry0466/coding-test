# e, s, b이 1씩 증가, 각 최댓값은 15 28 19

e, s, m = map(int, input().split())

ans = 1

e1, s1, m1 = 1, 1, 1
while True:

    if e == e1 and s == s1 and m == m1:
        print(ans)
        break

    ans+=1
    e1+=1
    s1+=1
    m1+=1

    if e1 > 15: e1 = 1
    if s1 > 28: s1 = 1
    if m1 > 19: m1 = 1

