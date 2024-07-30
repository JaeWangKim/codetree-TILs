n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

total = 0  
for i in range(1, n-m + 1):
    count = 0
    count2 = 0
    for k in range(m):
        if mat[i-1][i+k-1] == mat[i-1][i+k]:
            count +=2
        if mat[i+k-1][i-1] == mat[i+k][i-1]:
            count2 +=2
    if count >= m:
        total += 1
    if count2 >= m :
        total += 1
    
print(total)