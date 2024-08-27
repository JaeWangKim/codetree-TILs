n = int(input())

arr = [
    list(map(int, input().split())) for _ in range(n)
 ]
people = 0
people_total = []
house  = 0
visited = [
    [False]*n for _ in range(n)
]

def in_range(x,y):
    return 0<=x<=n-1 and 0<=y<=n-1

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True


def dfs(x, y):
    global people

    dxs, dys = [1,0,-1,0], [0,1,0,-1] #하 우 상 좌

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            people +=1 
            dfs(nx, ny)
            
      

for i in range(0, n):
    for j in range(0, n):
        if not visited[i][j] and arr[i][j] == 1:
            people = 1  # 새로운영역이므로 1시작
            visited[i][j] = True
            house += 1
            dfs(i, j)
            
            people_total.append(people)
           

people_total.sort() 

print(len(people_total))
for a in people_total:
    print(a)