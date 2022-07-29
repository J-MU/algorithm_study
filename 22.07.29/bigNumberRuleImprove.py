# 이것이 코딩테스트다 -나동빈저자 (Chapter3 그리디)
# p.92 큰수의 법칙
# 출처: 2019 국가 교육기관 코딩 테스트
listSize,totalSumCount,continiousLength=map(int,input().split())

numList=list(map(int,input().split()))
repeatSequence=list()
repeatSum=0

numList.sort(reverse=True)

# 반복되는 배열 초기화
# length: continiousLength+1
for i in range(continiousLength):
    repeatSequence.append(numList[0])
repeatSequence.append(numList[1])

repeatSequenceLength=len(repeatSequence)
repeatSum=numList[0]*continiousLength+numList[1]

repeatCount=totalSumCount//repeatSequenceLength
remainder=totalSumCount%repeatSequenceLength

partitionSum=0
for i in range(remainder):
    partitionSum+=repeatSequence[i]

sum=repeatCount*repeatSum+partitionSum

print(sum)

print(numList)