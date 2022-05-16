import sys

CONFERENCE_START_TIME=0
CONFERENCE_END_TIME=1

conference_count = int(sys.stdin.readline().rstrip())
candidate_conference_list=[]
selected_conference_list=[]

for i in range(conference_count):
    candidate_conference_list.append(list(map(int,sys.stdin.readline().rstrip().split())))

#정 안되면 이부분을 quicksort로 구현하는 방법 찾아보고
candidate_conference_list.sort(key= lambda x: x[0]) #O(nlogn)
candidate_conference_list.sort(key= lambda x: x[1]) #O(nlogn)
# 예약 후보 리스트에서 회의시작시간이 가장 이른 회의를 찾아 선택하는 함수.

print(candidate_conference_list)
selected_conference=candidate_conference_list[0]
count=1

for index in range(1,conference_count):
    if candidate_conference_list[index][CONFERENCE_START_TIME]>=selected_conference[CONFERENCE_END_TIME]:
        count+=1
        selected_conference=candidate_conference_list[index]

print(count)