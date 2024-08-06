# n, m = map(int, input().split())
# a = []

# def choose(curr_a, cnt):
#     if curr_a == m+1:


#     for i in range(1,n+1):
#         a.append(i)
#         choose(curr_a+1, cnt)
#         a.pop()
    
from itertools import combinations

n, m = map(int, input().split())
data = []
for i in range(1, n+1):
    data.append(i)


result= list(combinations(data, m))
for i in result:
    print(*i)