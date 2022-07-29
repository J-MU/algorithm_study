# 이것이 코딩테스트다 -나동빈저자 (Chapter3 그리디)
# p.99 1이 될 때까지
# 출처: 2018 E기업 알고리즘 대회

def minusOperation(num):
    return num-1

def divideOperation(num,K):
    return num//K

num,K=map(int,input().split())
operationCount=0

while(num>1):
    operationCount+=1
    if(num%K==0):
        num=divideOperation(num,K)
    else:
        num=minusOperation(num)
    print(operationCount,num)

print("operationCount:",operationCount)
