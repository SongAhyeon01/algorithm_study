''' N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마
구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대
값을 출력하는 프로그램을 작성하세요.'''

# 풀이 방법 : 이분 검색

n, c = map(int, input().split(' '))
a = [int(input()) for _ in range(n)]
res = 0
a.sort()

# 해당 거리를 두고 몇마리의 말이 들어가는 지 확인
def Count(len):
    cnt = 1
    ep = a[0] # 가장 최근에 말을 놓은 지점
    for i in range(1, n):
        if a[i]-ep >= len: # 말을 놓을 수 있다면
            cnt += 1
            ep = a[i] # 최근에 놓은 지점 변경

    return cnt

lt = 1
rt = a[n-1]

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)


