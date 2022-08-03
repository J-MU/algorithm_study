# 백준 1946번 문제(그래프 탐색문제)
# https://www.acmicpc.net/problem/1946


def setting(array):
    return array[0]

def minSetting(array):
    return array[1]

def next_index(false_array,index):
    for i in range(index+1,len(false_array),1):
        if(false_array[i]==0):
            return i
test_case_num=int(input())


for i in range(test_case_num):
    employee_num=int(input())
    array = list()
    true_count=1
    false_array=[0 for i in range(employee_num+1)]
    index=1

    for j in range(employee_num):
        paperwork_score,interview_score=map(int,input().split())
        array.append((paperwork_score,interview_score))

    array.sort(key=setting)

    # for k in range(len(array)):
    #     print(array[k])

    for n in range(employee_num-1,0,-1):
        if (array[n][1] == index):
            true_count += 1
            index=next_index(false_array,index)
        else:
            current_value=array[n][1]
            false_array[current_value]=1



    print(true_count)
