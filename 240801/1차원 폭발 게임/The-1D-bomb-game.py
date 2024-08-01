n, m = map(int, input().split())

array = [int(input()) for _ in range(n)]

# 1. 연속인지 체크하는, 2. 제거하는, 3.위치 끌어 내리는,  1,2번 기능을  chech함수에서 완성함

def check(arr, m):
    constant = 1

    for i in range(1, n):
        if arr[i-1] == arr[i]:
            constant += 1
            if i == n-1 and arr[i] == 0:
                constant = 1
                return arr, constant
        else:
            #만약 연속된 수가 m 이상이면 그냥 바로 그 구간을 0으로 제거해줘 현재 i는 연속되지 않은 순간이니 range()를 i-1까지 타도록 설정한 것
            if constant >= m:
                for j in range(i-constant, i):
                    arr[j] = 0
            else:
                constant = 1
    return arr, constant

def check_after(arr):
    n = len(arr)
    temp = [0] * n
    temp_row = 0
    for i in range(n):
        if arr[i] != 0:
            temp[temp_row] = arr[i]
            temp_row += 1
    for i in range(n):
        arr[i] = temp[i]
    
    return arr



while True:

    # 먼저 check()함수를 통해 연속된 부분을 확인하고 제거한다.
    arr_check, constant = check(array, m)
    # chech_after 함수를 통해 제거된 부분을 제외하고 아래로 떨어트린다.
    array = check_after(arr_check)

    arr_chech, constant = check(array, m)
    if constant == 1:
        break

print(len(list(a for a in array if a!=0)))
for i in array:
    if i != 0:
        print(i)