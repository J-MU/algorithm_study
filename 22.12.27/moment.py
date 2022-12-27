# 시간 #분 #초
# 시간 and 분 => 15
# 시간 and 초 => 15
# 분 and 초 => 225
# 시 and 분 and 초 => 225
# A type : 시간에 3이 안들어가는경우
 #  15*60 900 + 15 * 60 900 1800-225 1575
# B type : 시간에 3이 들어가는경우
 # 3600
#1ㅅ간 3600

#00시 00분 00초 ~ 5시간 59분 59초
# 0시 :1575 * 5 = 7875
#3시 : 3600
N=int(input())
count=0
for i in range(N+1):
    print(i)
    if(i==3):
       count=count+3600
    else:
        count=count+1575
print(count)