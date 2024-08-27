n,  m = map(int, input().split())

lis = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]


order = 1

def in_range(x,y):
    return 0<= x <= n-1 and 0<= y <= m-1

def can_go(x, y):
    if not in_range(x,y):
        return False
    if visited[x][y] and lis[x][y] == 0:
        return False
    return True


def dfs(x, y):
    global order
    dxs, dys = [1,0], [0,1] # 아래쪽이나 오른쪽 중 우선 방향이 있다면 그 방향 먼저 정의

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if can_go(nx, ny):
            lis[nx][ny] = order
            order += 1
            visited[nx][ny] = True
            dfs(nx, ny)

lis[0][0] = order
order += 1
visited[0][0] = True
dfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)