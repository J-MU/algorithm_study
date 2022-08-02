# 이것이 코딩테스트다 -나동빈저자 (Chapter3 그리디)
# p.92 큰수의 법칙
# 출처: 2019 국가 교육기관 코딩 테스트
listSize,totalSumCount,continiousLength=map(int,input().split())

numList=list(map(int,input().split()))

numList.sort(reverse=True)
sum=0
count=0
maxNumberIndex=0

for i in range(totalSumCount):
    if(count==continiousLength):
        sum+=numList[maxNumberIndex+1]
        count=0
        continue
    sum+=numList[maxNumberIndex]
    count+=1

print(sum)
print(numList)

