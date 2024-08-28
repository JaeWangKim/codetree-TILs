from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().rstrip().split())

grid = [
    list(map(int, input().rstrip().split())) for _ in range(n)
]

visited = [
    [False]*m for _ in range(n)
]

q = deque()

order = 0


def in_range(x, y):
    return 0<= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def push(x, y, order):
    visited[x][y] = True
    grid[x][y] = order 
    q.append((x, y))

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                push(nx, ny, grid[x][y]+1)

push(0,0,0)
bfs()

if visited[n-1][m-1]:
    print(grid[n-1][m-1])
else:
    print(-1)