n, m = map(int, input().split())

a = list(map(int, input().split()))
an =[]
max_total = 0
def choose(curr_a):
    global max_total
    total =0
    if curr_a == m + 1:
        for i in range(m):
            total ^= an[i]
        max_total = max(int(total), max_total)
        return
        
    
    for i in a:
        an.append(i)
        choose(curr_a + 1)
        an.pop()
choose(1)
print(max_total)