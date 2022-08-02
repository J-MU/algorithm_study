# 이것이 코딩테스트다 -나동빈저자 (Chapter4 구현)
# p.113 시각


class currentTime:
    cur_second=0
    cur_minute=0
    cur_hour=0

    def __str__(self):
        return "{0} : {1} : {2} ".format(self.cur_hour,self.cur_minute,self.cur_second)

def plusOneSecond():
    if curTime.cur_second+1>=60:
        curTime.cur_second=0
        if curTime.cur_minute+1>=60:
            curTime.cur_minute=0
            curTime.cur_hour+=1
        else:
            curTime.cur_minute+=1
    else:
        curTime.cur_second+=1

def checkHour(): # 1: 3이 속해있음 0: 3이 안 속해있음
    first_digit=curTime.cur_hour//10
    second_digit=curTime.cur_hour%10
    if(first_digit==3 or second_digit==3):
        return 1
    else:
        return 0

def checkMinute(): # 1: 3이 속해있음 0: 3이 안 속해있음
    first_digit=curTime.cur_minute//10
    second_digit=curTime.cur_minute%10
    if(first_digit==3 or second_digit==3):
        return 1
    else:
        return 0

def checkSecond(): # 1: 3이 속해있음 0: 3이 안 속해있음
    first_digit=curTime.cur_second//10
    second_digit=curTime.cur_second%10
    if(first_digit==3 or second_digit==3):
        return 1
    else:
        return 0

target_hour=int(input())
curTime=currentTime()
count=0
while(curTime.cur_hour<=target_hour):
    if(checkHour()):        # 시간에 3이 있는 경우.
        print(curTime,count)
        count+=3600
        curTime.cur_hour+=1
        print(curTime,count)
    elif(checkMinute()):    #분에 3이 있는 경우
        print(curTime,count)
        count+=60
        curTime.cur_minute+=1
        print(curTime,count)
    elif(checkSecond()):    #초에 3이 있는 경우
        count+=1
        print(curTime,count)
        plusOneSecond()
    else:
        plusOneSecond()

print(count)

