# n과 k 가 주어졌을 때 n의 약수들 중 k번째 약수 구하기

n, k = map(int, input().split(' '))

li = []
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)

if k > len(li):
    print(-1)
else:
    print(li[k-1])