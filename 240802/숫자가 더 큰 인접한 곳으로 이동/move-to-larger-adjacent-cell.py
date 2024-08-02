n, r, c = map(int, input().split())

c_x = r -1
c_y = c -1


array = [
    list(map(int, input().split())) for _ in range(n)
    ]

def in_range(x, y):
    return 0<= x and x<=n-1 and 0 <= y and y <= n-1

def simulate(arr):
    global c_x, c_y

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    c_num = arr[c_x][c_y]
    n_num = c_num
    c_pos = (c_x, c_y)
    a = 0
    for dx, dy in zip(dxs, dys):
        n_x = c_x + dx
        n_y = c_y + dy
        
        if in_range(n_x, n_y) and c_num < arr[n_x][n_y]:
            if a != 1:
                n_num = arr[n_x][n_y]
                c_x, c_y = n_x, n_y
                a = 1
                
    if c_num == n_num:
        return 0
    else:      
        return 1
print(array[c_x][c_y], end=' ')
while True:
    if simulate(array) == 1:
        print(array[c_x][c_y], end=' ')
    else:
        break