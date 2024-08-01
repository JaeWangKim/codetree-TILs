n = int(input())

temp1 = [0]*n
temp2 = [0]*n
temp1_end = 0
temp2_end = 0
array = []
for _ in range(n):
    array.append(int(input()))
# temp 만듬


s1, e1 = map(int, input().split())
s2, e2  = map(int, input().split())

s1 -= 1
e1 -= 1
s2 -= 1
e2 -= 1

for i in range(s1, e1+1):
    array[i] = 0

for i in range(n):
    if array[i] != 0:
        temp1[temp1_end] = array[i]
        temp1_end += 1

for i in range(n):
    array[i] = temp1[i]

for i in range(s2, e2+1):
    array[i] = 0

for i in range(n):
    if array[i] != 0:
        temp2[temp2_end] = array[i]
        temp2_end += 1
    
for i in range(n):
    array[i] = temp2[i]

print(len(list(a for a in array if a!=0)))
for i in array:
    if i !=0:
        print(i)