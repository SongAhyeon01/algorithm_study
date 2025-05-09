'''엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이
다. 선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을
잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면
20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.). 필요한 랜선 개수는 N'''

# 풀이 방법 : 이분검색

# 해당 길이로 잘랐을 때 이 랜선으로는 몇 개 만들 수 있는 지
def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len) #각각의 랜선을 자른 랜선의 길이로 나눈 몫
    return cnt


k, n = map(int, input().split(' '))
line = [int(input()) for _ in range(k)]
res = 0 # 현재 정답
largest=max(line) # 가장 긴 길이

lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2 # 랜선 1개의 길이
    if Count(mid) >= n: # 개수가 맞거나 많으면
        res = mid
        lt = mid+1 # 더 긴 답을 찾아서 나간다
    else: # 길이가 너무 길어서 개수가 안나온다면
        rt = mid-1

print(res)




