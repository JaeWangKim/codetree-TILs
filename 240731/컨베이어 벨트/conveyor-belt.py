n,t = map(int, input().split())

up = list(map(int, input().split()))
down = list(map(int, input().split()))

up.extend(down)

for i in range(t):
    temp = up[-1]
    for j in range(2*n-1, 0, -1):
        up[j] = up[j-1]
    up[0] = temp 
a = len(up)/2

print(*up[:int(a)])
print(*up[int(a):])