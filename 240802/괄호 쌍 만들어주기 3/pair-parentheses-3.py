a = input()
count = 0
for index, i in enumerate(a):
    if i == '(':       
        for j in a[index+1:len(a)]:
            if j == ')':
                    count+=1
    

print(count)