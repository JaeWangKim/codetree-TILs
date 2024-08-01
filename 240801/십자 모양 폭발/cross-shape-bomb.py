n = int(input())

array = [
    list(map(int, input().split())) for _ in range(n)
]

r,c = map(int, input().split())

r -= 1
c -= 1

def boomb_after(arr):
    temp = [
        [0]*n for _ in range(n)
    ]
    
    for j in range(n):
        temp_row = n-1
        for i in range(n-1, -1, -1):
            if arr[i][j] != 0:
                temp[temp_row][j] = arr[i][j]
                temp_row -= 1
    for j in range(n):
        for i in range(n):
            arr[i][j] = temp[i][j]


    return arr

def boomb(arr, boomb_x, boomb_y):
    a = arr[boomb_x][boomb_y]
    a -= 1
    #행에 대해서 먼저 제거하기
    for i in range(boomb_y-a, boomb_y+a+1):
        arr[boomb_x][i] = 0
    #열에 대해 제거하기
    for i in range(boomb_x-a, boomb_x+a+1):
        arr[i][boomb_y] =0

    return arr

boomb_array = boomb(array, r, c)

temp_use_array = boomb_after(boomb_array)

for i in range(n):
    for j in range(n):
        print(temp_use_array[i][j], end=' ')
    print('')