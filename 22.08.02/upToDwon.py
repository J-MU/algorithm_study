# 이것이 코딩테스트다 -나동빈저자 (Chapter6 정렬)
# p.178 위에서 아래로
# 출처: ??
# 08.02

array=list()

array_size=int(input())

for i in range(array_size):
    array.append(int(input()))

array.sort(reverse=True)
print(array)