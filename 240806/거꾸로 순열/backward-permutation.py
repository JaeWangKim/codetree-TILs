n = int(input())

arr = list(range(1, n+1))
arr_mid = []
arr_final = []
visited = [False]*(n+1)


def choose(curr_a):
    if curr_a == n+1:
        arr_final.append(list(arr_mid))
        return 
     
    for i in range(1, n+1):
        if visited[i] == True:
            continue

        arr_mid.append(i)
        visited[i] = True

        choose(curr_a +1)

        arr_mid.pop()
        visited[i] = False
        
        
choose(1)
arr_final.sort(reverse = True)
for i in arr_final:
    print(*i)