n = input()
arr = {}

for i in range(0, len(n), 2):
    arr[n[i]] = 1
res = -(2**31)

def compute_and_compare(curr_a):
    global res
    val = curr_a[n[0]]

    for i in range(1, len(n), 2):
        if n[i] == '+':
            val += curr_a[n[i+1]]
        if n[i] == '-':
            val -= curr_a[n[i+1]]
        if n[i] == '*':
            val *= curr_a[n[i+1]]
    res = max(res, val)

def check_combs(curr_a):
    compute_and_compare(curr_a)

    for k in arr.keys():
        if curr_a[k] >= 4:
            continue
        curr_a[k] += 1
        check_combs(curr_a)
        if curr_a[k] == 1:
            curr_a[k] = 1
        else: 
            curr_a[k] -=1
    
check_combs(arr)
print(res)