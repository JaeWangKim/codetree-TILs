n = int(input())

arr = list(range(1, n+1))
arr_mid = []
visited = [False]*(len(arr)+1)
arr_final = []

# 하나씩 선택해서 배열을 만들기. 이떄, 멈춰야 하는 길이는 n+1에 멈추면서 리턴, 이때, 이런하지말고 리스트에 저장했다가 sort하자
def choose(curr_num):
    if curr_num == n+ 1:
        arr_final.append(arr_mid[:])
        return 

    for i in range(1, n+1):
        if visited[i] == True:
            continue
        #현재 확인하는 값을 추가해 순열을 만들고 사용한 수는 방지처리
        arr_mid.append(i)
        visited[i] = True

        choose(curr_num +1)
        
        arr_mid.pop()
        visited[i] = False

choose(1)
arr_final.sort()

for i in arr_final:
    print(*i)