# 이것이 코딩테스트다 -나동빈저자 (Chapter6 정렬)
# p.182
# 출처: 성적이 낮은 순서로 학생 출력하기
# 08.02

n,k=map(int,input().split())
array_A=list(map(int,input().split()))
array_B=list(map(int,input().split()))

array_A.sort()
array_B.sort(reverse=True)
print("swap 전")
print(array_A)
print(array_B)


for i in range(k):
    array_A[i],array_B[i]=array_B[i],array_A[i]

print("swap 후")
print(array_A)
print(array_B)

sum=0

for i in range(n):
    sum+=array_A[i]

print(sum)
