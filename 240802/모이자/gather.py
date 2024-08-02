import sys
n = int(input())
a = list(map(int, input().split()))



MAX = sys.maxsize

min_sum = 0 
# 0번째부터 장소로 지정
for i in range(n):
    #이제는 i번째 집이라고 가정하에 각 이동 값계산 및 최소값 업데이트   
    sum_diff = 0
    for j in range(n):
        sum_diff += abs(j-i)*a[j]
       
    min_sum = min(MAX, sum_diff)
    MAX = min_sum

print(min_sum)