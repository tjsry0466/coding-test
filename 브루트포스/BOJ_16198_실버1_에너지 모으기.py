# n개의 구슬중에서 맨앞과 맨 뒤를 제외하고 한개의 구슬을 뽑은뒤
# 해당 번호 구슬을 제거하고 앞 뒤 의 구슬만큼 모을수 있다.
# 여러번 반복했을때 최대로 모을수 있는 구슬을 구하는 문제

n = int(input())
a = list(map(int, input().split()))

def go(a):
    n = len(a)
    if n == 2:
        return 0
    ans = 0
    for i in range(1, n-1):
        energy = a[i-1] * a[i+1]
        b = a[:i] + a[i+1:]
        energy += go(b)
        if ans < energy:
            ans = energy
    return ans

print(go(a))