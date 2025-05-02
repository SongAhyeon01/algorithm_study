'''문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이
됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다.  출력은 120를 출력하고, 다음 줄에 120
의 약수의 개수를 출력하면 됩니다'''

# 앞의 0삭제
def delete_0(nums_li):

    while nums_li[0] != '0':
        nums_li.pop(0)

    nums = int(nums_li)

    return nums

# main
st = input()
nums_li = ''

for i in st:
    if i.isnumeric():
        nums_li += i

nums = delete_0(nums_li)


# 약수 개수 구하기
cnt = 0
for j in range(1, nums+1):
    if nums % j == 0:
        cnt += 1

print(f'{nums} 의 약수의 개수는 {cnt}')




