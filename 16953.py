input_list=input().split()
initial_value=int(input_list[0])

final_value_str=input_list[1]


count=0
while initial_value<int(final_value_str):
    count+=1

    if initial_value==int(final_value_str):
        print('count: ',count)
    if int(final_value_str)%2==0:
        final_value_str=str(int(final_value_str)//2)
        print(final_value_str)
    elif final_value_str[-1]=='1':
        final_value_str=final_value_str[:-1]
        print(final_value_str)
    else:
        print(-1)
