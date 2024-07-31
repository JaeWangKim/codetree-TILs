n , t = map(int, input().split())

l_u = list(map(int,input().split()))
r_u = list(map(int,input().split()))
d = list(map(int,input().split()))


total = l_u + r_u + d

for i in range(t):
    temp = total[0]
    for j in range(3*n-1, 0, -1):
        total[j] = total[j-1]
    
    total[0] = temp

print(*total[:n])
print(*total[n:2*n])
print(*total[2*n:])