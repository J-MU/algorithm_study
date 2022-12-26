list_size=int(input())
score=list(map(int,input().split()))

max_int=max(score)
sum=0
for i in range(len(score)):
    sum+=score[i]

avg=sum/len(score)

print(avg*(100/max_int))