'''N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.'''
# 부분수열

n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
tot = a[0] # 부분의 합
lt = 0 # 왼쪽 끝
rt = 1 # 오른쪽 끝
cnt = 0 #개수

while True:
    if tot < m: # 부분의 합이 찾으려는 수보다 작으면
        if rt < n: # 다만, 리스트의 마지막이 아니면
            tot += a[rt] # 부분의 합에 오른쪽 값 더하기
            rt += 1 # 오른쪽 끝을 한 칸 이동
        else:
            break
    elif tot == m: # 부분의 합이 찾으려는 수와 같으면
        cnt += 1 # 찾았으므로 카운트 증가
        tot -= a[lt] # 현재 왼쪽 끝이 가리키는 값 빼기
        lt += 1 # 왼쪽 끝을 한 칸 이동
    else:
        tot -= a[lt] # 현재 왼쪽 끝이 가리키는 값 빼기
        lt += 1 # 왼쪽 끝을 한 칸 이동
print(cnt)





