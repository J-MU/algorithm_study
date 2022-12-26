list_size=int(input())
rope_list=[]

for i in range(list_size):
    rope_list.append(int(input()))

rope_list.sort()
max_weight=0
cur_weight=0

rope_list.sort(reverse=True)
#하나씩 받아와서 최대 n까지 중량이 w인 물체를 k로 나눠서 젤 작은애*k값 변화확인
for i,j in zip(list(rope_list),range(len(rope_list))):
    cur_weight=i*(j+1)
    if(max_weight<cur_weight):
        max_weight=cur_weight

print(max_weight)