# 재귀함수 풀이 방법
n = int(input())
a = list(map(int, input().split()))
check = [False] * ((n*100000)+10)
def go(i, s):
    if i == len(a):
        check[s] = True
        return

    go(i+1, s)
    go(i+1, s+a[i])

go(0, 0)

z = 0
while True:
    if check[z] == False:
        print(z)
        break
    z +=1


# 비트 마스크 풀이 방법

# n = int(input())
# a = list(map(int, input().split()))
# c = [False] * (n*100000+10)
# for i in range(1<<n):
#     s = 0
#     for j in range(n):
#         if (i&(1<<j)):
#             s += a[j]
#     c[s] = True
# i = 1
# while True:
#     if c[i] == False:
#         break
#     i +=1
# print(i)