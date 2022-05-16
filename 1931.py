import sys

CONFERENCE_START_TIME=0
CONFERENCE_END_TIME=1

#conference_count=int(input())
conference_count = int(sys.stdin.readline().rstrip())
candidate_conference_list=[]
selected_conference_list=[]

for i in range(conference_count):
    candidate_conference_list.append(list(map(int,sys.stdin.readline().rstrip().split())))

#여기까지는 더 줄이기 힘듬
######################################

#정 안되면 이부분을 quicksort로 구현하는 방법 찾아보고
candidate_conference_list.sort(key= lambda x: x[1],reverse=True) #O(nlogn)
# 예약 후보 리스트에서 회의시작시간이 가장 이른 회의를 찾아 선택하는 함수.

def select_conference():
    selected_conference=candidate_conference_list.pop()
    selected_conference_list.append(selected_conference)
    return selected_conference

# 선택 불가능한 회의 제거
# select_conference의 회의 종료시간보다 회의 시작시간이 빠른 후보는 탈락이다.
# def remove_dropout_conference(for_loop_count,selected_conference):
#     index=0
#     for i in range(for_loop_count):
#         candidate_conference=candidate_conference_list[index]
#         if candidate_conference[CONFERENCE_START_TIME]<selected_conference[CONFERENCE_END_TIME]:
#             candidate_conference_list.remove(candidate_conference)
#         else:
#             index+=1

#진짜 고민을 많이 해봤는데 되는 애를 빈 배열에 옮기는게 더 빠를 수도 있겠다.
def remove_dropout_conference(for_loop_count,selected_conference):
    temp_list=[]
    for index in range(for_loop_count):
        candidate_conference=candidate_conference_list[index]
        if candidate_conference[CONFERENCE_START_TIME]>=selected_conference[CONFERENCE_END_TIME]:
            temp_list.append(candidate_conference)
    return temp_list

while len(candidate_conference_list)!=0:
    selected_conference=select_conference()
    candidate_conference_list=remove_dropout_conference(len(candidate_conference_list),selected_conference)

print(len(selected_conference_list))