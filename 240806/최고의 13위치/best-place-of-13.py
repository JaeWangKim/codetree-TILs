n = int(input())

matrix = [
    list(map(int, input().split())) for _ in range(n)
]

def in_range(x, y):
    return 0<= x<= n-1 and 0 <= y <= n-3

def check():
    max_count = 0
    for i in range(n):
        for j in range(n):
            if in_range(i, j):
                count = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]
                max_count = max(max_count, count)
    return max_count 

print(check())