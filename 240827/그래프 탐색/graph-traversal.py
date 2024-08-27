n, m = map(int, input().split())

lis = [list(map(int, input().split())) for _ in range(m)]

visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]
cnt = 0
def dfs(vertex):
    global cnt
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)


for start_p, end_p in lis:
    graph[start_p].append(end_p)
    graph[end_p].append(start_p)

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(cnt)