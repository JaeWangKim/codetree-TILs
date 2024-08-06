from sys import stdin
n, m = list(map(int, stdin.readline().split()))
number = list(map(int, stdin.readline().split()))

base = []
def choose(curr_num, idx): #curr_num번째 자리에 들어갈 차례이며 number의 idx까지 뽑음
    if curr_num == m+1: #m개 뽑은 후에 끝
        result = base[0]
        for i in range(1, m):
            result = result ^ base[i]
        # print(base, result)
        return result
    
    ans = 0
    for i in range(idx+1, n): #idx+1~n-1까지 숫자를 가져옴
        base.append(number[i])
        ans = max(ans, choose(curr_num+1, i))
        base.pop()
    return ans

print(choose(1,-1))