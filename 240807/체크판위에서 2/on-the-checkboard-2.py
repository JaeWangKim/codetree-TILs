import sys
input = sys.stdin.readline
r, c = map(int, input().split())

array = [
    list(input().split()) for _ in range(r)
]

#  방문위치 기억, 이전 문자 색 기억 다 필요없고, 무조건 오른쪽 아래로 이동해야 하는 걸 이용하려면  4중 for문함련 모두 해결된다.

cnt = 0
for i in range(1,r):
    for j in range(1,c):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if array[0][0] != array[i][j] and \
                    array[i][j] != array[k][l] and \
                    array[k][l] != array[r-1][c-1]:
                        cnt += 1

print(cnt)