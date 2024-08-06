#from itertools import permutations

n = int(input())

arr = list(map(int, input().split()))
arr_mid = []
count = 0
visited= [False]*n


def compare():
    global count
    if arr_mid[0] <= arr_mid[1] <= arr_mid[2]:
        count += 1
        return
    else:
        return

def choose(curr_a, num):
    if curr_a == 4:
        compare()
        return

    for index, i in enumerate(arr):
        if visited[index] == True or index<=num:
            continue
        arr_mid.append(i)
        visited[index] = True

        choose(curr_a+1, num+1)

        arr_mid.pop()
        visited[index] = False
        if len(arr_mid) == 0:
	        num += 1

choose(1, 0)
print(count)