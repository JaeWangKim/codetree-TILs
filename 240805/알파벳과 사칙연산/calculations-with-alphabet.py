exps = list(input())

alpha = []

exp = []

for e in exps:
    if e.isalpha():
        alpha.append(e)
    else:
        exp.append(e)
alpha = list(set(alpha))
alpha_mapping = {
    a: 0
    for a in set(alpha)
}

result = 0

selected = []

def calculate():
    global selected
    global alpha_mapping
    for i, k in enumerate(alpha_mapping.keys()):
        alpha_mapping[k] = selected[i]

    r = alpha_mapping[alpha[0]]

    for i, ex in enumerate(exp):
        a = alpha[i + 1]
        if ex == "-":
            r = r - alpha_mapping[a]
        elif ex == "+":
            r = r + alpha_mapping[a]
        elif ex == "*":
            r = r * alpha_mapping[a]
    
    return r

def select(idx):
    global result
    if idx == len(alpha):
        result = max(result, calculate())
        return

    for i in range(1, 5):
        selected.append(i)
        select(idx + 1)
        selected.pop()

select(0)

print(result)