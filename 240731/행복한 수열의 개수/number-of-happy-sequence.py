n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

total = 0  
for i in range(1, n-m + 1):
    count = 1
    count2 = 1
    for k in range(m):
        if m != 1:
            if mat[i-1][i+k-1] == mat[i-1][i+k]:
                count +=1
            if mat[i+k-1][i-1] == mat[i+k][i-1]:
                count2 +=1
        else:
            count = n
            count2 = n
    if count >= m:
        total += 1
    if count2 >= m :
        total += 1
    
print(total)