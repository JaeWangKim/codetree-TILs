from collections import deque
n, m = map(int, input().split())

grid = [
    list(map(int, input().split())) for _ in range(n)
]

visited = [
    [False]*m for _ in range(n)
]

order = 1

q = deque()

def in_range(x, y):
    return 0 <= x < n and 0<= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def push(x, y):
    global order
    
    grid[x][y] = order
    order += 1
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dxs, dys = [1,0, -1, 0], [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                push(nx, ny)

push(0,0)
bfs()
if visited[n-1][m-1]:
    print(1)
else:
    print(0)