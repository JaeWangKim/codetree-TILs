n, m = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]


max_case1 = 0 
max_case2 = 0 
max_case3 = 0 
max_case4 = 0 
max_case5 = 0 
max_case6 = 0 

for x in range(n):
    for y in range(m):        
        if 1 <= y <= m-1 and 1 <= x <= n-1:
            case1 = mat[x][y] + mat[x-1][y] + mat[x][y]
            if case1 > max_case1:
                max_case1 = case1
        if 1 <= x < n-1 and 0 <= y <= m-2:
            case2 = mat[x-1][y] + mat[x][y] + mat[x][y+1]
            if case2 > max_case2:
                max_case2 = case2
        if 0 <= x <= n-2 and 0 <= y <= m-2:
            case3 = mat[x][y] + mat[x][y+1] + mat[x+1][y]
            if case3 > max_case3:
                max_case3 = case3
        if 0 <= x <= n-2 and 1 <= y <= m-2:
            case4 = mat[x][y] + mat[x][y-1] + mat[x+1][y]
            if case4 > max_case4:
                max_case4 = case4
        if 0 <= x <= n-1 and 0 <= y <= m-3:
            case5 = mat[x][y] + mat[x][y+1] + mat[x][y+2]
            if case5 > max_case5:
                max_case5 = case5
        if 0 <= x <= n-3 and 0 <= y <= m-1:
            case6 = mat[x][y] + mat[x+1][y] + mat[x+2][y]
            if case6 > max_case6:
                max_case6 = case6

total_max = max(max_case1, max_case2, max_case3, max_case4, max_case5, max_case6)
print(total_max)