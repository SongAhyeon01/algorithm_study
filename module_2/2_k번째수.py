# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를
# 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.

T = int(input())

for i in range(1):
    N, s, e, k = map(int, input().split(' ')) # 길이 N의 배열에서 s부터 e번째 요소를 오름차순 정렬했을 때 k번째 숫자
    li = list(map(int, input().split(' ')))
    li_se = li[s-1:e]
    li_se = sorted(li_se)
    print(li_se[k-1])