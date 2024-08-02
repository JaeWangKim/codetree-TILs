n, m, k = map(int, input().split())

array = [
    list(map(int, input().split())) for _ in range(n)
]
k -= 1
c_col = k
c_row = -1
count = 0
# 1. 블럭 범위에 있는지 확인하는 함수 , 2. 상하좌우에서 하만 사용해서 내리는데, m개수만큼의 블럭을 for문으로 내리는 함수(하나라도 못움직이면 브레이크)
def in_range(x, y):
    return 0<= x<= n-1 and 0<= y <= n-1

def can_move():
    pass
def simulate(arr):
    global c_col,c_row, m, count
    for row in range(-1, n):
        for col in range(0,0+m):
            c_row = row
            n_x = c_row +1
            n_y = col
            if in_range(n_x, n_y) and arr[n_x][n_y] != 1:
                c_col = n_y
                c_row = n_x
                arr[c_row][c_col] = 1
                if row > -1:
                    arr[c_row-1][c_col] = 0            
            else: 
                return 0
            
    
    return 1 

       
while True:
    a = simulate(array)
    # a가 True이면 이동 했음을 의미하므로 이동한 자리를 1표시 해준다. 그리고 내려온 자리인 이전 자리는 0으로 표시해준다.
    if a:
        pass
    else:
        for i in range(n):
            for j in range(n):
                print(array[i][j], end=' ')
            print('')
        break