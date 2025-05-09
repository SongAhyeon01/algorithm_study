'''임의의 N개의 숫자가 입력으로 주어집니다.  N개의 수를 오름차순으로 정렬한 다음 N개의 수
중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
프로그램을 작성하세요. 단 중복값은 존재하지 않습니다.'''

n, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

a.sort()

lt = 0
rt = n-1

while lt <= rt:
    mid = (lt+rt)//2
    if a[mid] == m: # 숫자를 찾았다면
        print(mid+1)
        break
    elif a[mid] > m: # 찾고자 하는 값이 작은 쪽에 있음
        rt = mid-1
    else: # 찾고자 하는 값이 큰 쪽에 있음
        lt = mid+1
