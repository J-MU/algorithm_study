# programmers 코테연습kit의 스택/큐 프린터 문제
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

priorities=[1,1,9,1,1,1]
location=0
# priorities=[2,1,3,2]
# location=2

deque_priorities=deque(priorities)

print('deque:',deque_priorities)

# 우선순위는 0~9까지로 이루어져있고 이를 index 0~9에 사상한다.
# 배열의 값은 그 우선순위를 가진 task의 개수를 나타낸다.
priority_count_arr=[0 for i in range(10)]
print(priority_count_arr)

for i in range(len(priorities)):
    priority_count_arr[priorities[i]]+=1

print(priority_count_arr)
print("len: ",len(deque_priorities))
count=0 # pop할때마다 count 몇번째로 실행되는지를 나타냄
key=False   # 반복문을 나가는 조건(첫번째 for문)

for i in range(9,0,-1):
    if key:
        break;
    if priority_count_arr[i]!=0:
        while priority_count_arr[i]>0:
            if deque_priorities[0]==i:
                if location==0:
                    count+=1
                    key=True
                    break;
                deque_priorities.popleft()
                location-=1
                count+=1
                priority_count_arr[i]-=1
            else:
                temp=deque_priorities.popleft()
                deque_priorities.append(temp)
                if location==0:
                    location=len(deque_priorities)-1
                else:
                    location-=1
    else:
        continue

print(count)

# count: location에 위치한 문서가 몇번째로 인쇄될 지를 return 해준다.