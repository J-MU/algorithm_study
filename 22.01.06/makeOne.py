list=[]
d=[0]*30000
# d[1]=1
def makeOne(x,count):
    for i in range(1,x+1):
        if d[i+1] == 0 or d[i+1]>d[i]+1:
            d[i + 1] = d[i]+1
        if d[i*2] == 0 or d[i*2]>d[i]+1:
            d[i*2]=d[i]+1
        if d[i*3] == 0 or d[i*3]>d[i]+1:
            d[i*3]=d[i]+1
        if d[i*5] == 0 or d[i*5]>d[i]+1:
            d[i*5]=d[i]+1


x=int(input())
makeOne(x,0)
print(d[26])