n = int(input())

arr = list(map(int, input().split()))
count =0

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            if arr[i] <= arr[j] <= arr[m]:
                count+=1
print(count)