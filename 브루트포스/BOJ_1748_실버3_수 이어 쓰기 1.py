# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
# 이렇게 만들어진 수는 몇 자리수 일지 구하는 문제

# 1부터 9까지는 +1
# 10부터 99까지는 +2
# 100부터 999까지는 + 3
# 1000부터 9999까지는 +4

# 1자리 수이면 1~9
# 2자리 수이면 100~999
# 3자리 수이면 1000~9999

n = int(input())

ans = 0
start = 1
length = 1
while start <= n:
    end = start*10-1
    if end > n:
        end = n
    ans += (end-start+1) * length
    start *=10
    length +=1
print(ans)