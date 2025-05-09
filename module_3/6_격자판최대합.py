''' N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.'''

n = int(input())
a = [list(map(int, input().split(' '))) for _ in range(n)]

max_num = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j] #행
        sum2 += a[j][i] #열
    if sum1>max_num:
        max_num = sum1
    if sum2>max_num:
        max_num = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i] #왼쪽 대각선 a[0][0]
    sum2 += a[i][n-i-1] #오른쪽 대각선 a[0][4]
if sum1>max_num:
    max_num = sum1
if sum2>max_num:
    max_num = sum2

print(max_num)




