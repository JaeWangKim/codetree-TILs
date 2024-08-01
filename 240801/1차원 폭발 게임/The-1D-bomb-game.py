# 내가 푼 거
n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

#연속된거 개수 세주기
def get_counts(arr):
    cnt = 0
    num = len(arr)
    counts = [0] * num
    for i in range(num-1, 0, -1):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            cnt = 0
        counts[i] = cnt

    return counts

#폭탄이 터질수 있는 조건인지 확인하기
def can_bomb(counts, m):
    return any(i >= m-1 for i in counts)

#터지는 인덱스 범위로 1로 만들고 1이 아닌 것들만 저장해서 내보내기
def bomb(arr, counts, m):
    if m == 1:
        return []
    num = len(arr)
    bombed = [0] * num
    for i, cnt in enumerate(counts):
        if cnt >= m-1:
            for j in range(i-1, i+cnt):
                bombed[j] = 1
    return [arr[i] for i in range(num) if not bombed[i]]


while True:
    #현재 리스트에서 연속된게 있는지 파악
    cnts = get_counts(arr)
    #폭탄이 터질수 있는게 없다면 종료
    if not can_bomb(cnts, m):
        break
    arr = bomb(arr, cnts, m)

print(len(arr))
for i in arr:
    print(i)