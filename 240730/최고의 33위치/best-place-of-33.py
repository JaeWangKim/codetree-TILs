import sys
input = sys.stdin.readline

n = int(input())

mat = []

for i in range(n):
    mat.append(list(map(int, input().split())))

max_total = 0
total = 0
for i in range(n-2):
    for j in range(n-2):
        total = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j] + mat[i+1][j+1] + mat[i+1][j+2] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
        if total > max_total:
            max_total = total
        total = 0

print(max_total)