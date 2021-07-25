arr = [int(input()) for _ in range(9)]
arr.sort()
hap = sum(arr)

answer = (0, 0)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (hap - arr[i] - arr[j]) == 100:
            answer = (arr[i], arr[j])
            break

arr.remove(answer[0])
arr.remove(answer[1])
for i in arr:
    print(i)
