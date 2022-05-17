# https://programmers.co.kr/learn/courses/30/lessons/42586
# programmers 코테연습 stack파트 기능개발 문제
import math #ceil(올림)함수를 위해 import

#progress=list(map(int,input().split()))  #원소는 100개 이하
#speeds=list(map(int,input().split()))    #원소는 100개 이하.
progress=[99,99,99]
speeds=[1,1,1]

#
#   progress=[93 30 55]
#   speeds=[1,30,5]
#   남은 날=[7,3,9]일 임을 알 수 있다.
#   이 남은날은 math.ceil((100-progress)/speeds)를 통해 구할 수 있다.

remainder_days=list() #progresses와 speeds를 비교하여 작업이 완료되기까지 남은 날을 저장.
release_arr=list()  #배포된 작업의 개수를 저장

for i in range(len(progress)):
    remainder_day=math.ceil((100-progress[i])/speeds[i])
    print(remainder_day)
    remainder_days.append(remainder_day)


#print(remainder_days)

release_count=1 # 오늘 몇개의 작업이 배포 되었는지를 count
index=1 #작업 target
today_work=remainder_days[0]

while index<len(remainder_days):

    if(today_work>=remainder_days[index]):
        release_count+=1
        if index == len(remainder_days) - 1:
            release_arr.append(release_count)
    else:
        release_arr.append(release_count)
        release_count=1
        today_work=remainder_days[index]
        if index == len(remainder_days) - 1:
            release_arr.append(release_count)

    index += 1


print(release_arr)