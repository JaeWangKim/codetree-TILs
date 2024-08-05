n = int(input())

answer = []
total = 0

def choose(curr_num):
    global total
    if curr_num == n+1:
        total += check()
        return 
    for i in range(1, 5):        
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()
    return

def check():
    #연달아 같은 숫자가 나오는 시작 위치를 0으로 잡음
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        #아름다운 수가 아니니false, 3이면 3번 나올 공간을 확인
        if i+answer[i] - 1>= n:
            return 0
        
        #연속하여 해당 숫자만큼 같은 숫자가 있는지
        #하나라도 다르면 아름다운수가 아님
        for j in range(i, i+answer[i]):
            if answer[j] != answer[i]:
                return 0
        i += answer[i]
    return 1
choose(1)
print(total)