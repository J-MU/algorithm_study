# 이것이 코딩테스트다 -나동빈저자 (Chapter3 그리디)
# p.96 숫자 카드 게임
# 출처: 2019 국가 교육기관 코딩 테스트
N,M = map(int,input().split())
arr=list()
MaxOfMin=None
rowMin=None
minIndex=0

for i in range(N):

    arr.append(list(map(int,input().split())))
    rowMin=min(arr[i])
    if (i == 0):
        MaxOfMin =rowMin

    if(rowMin>MaxOfMin):
        MaxOfMin=rowMin
        maxIndex=i


print(N,M)
print(arr)
print("max: ",MaxOfMin)
print("maxIndex: :",maxIndex)