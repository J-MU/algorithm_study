array_size=int(input())

map= [[0]*array_size for i in range(array_size)];
direction_list=input();

cur_row=1;
cur_col=1;

def return_direct_point(index):
    if direction_list[index]=='R':
        return [0,1];
    elif direction_list[index]=='L':
        return [0,-1];
    elif direction_list[index]=='U':
        return [-1,0];
    elif direction_list[index]=='D':
        return [1,0]


for i in range(len(direction_list)):
    sum_row,sum_column=return_direct_point(i);
    print(sum_row,sum_column);
    print('row:',cur_row+sum_row);
    print('col:',cur_col+sum_column);
    if(cur_row+sum_row<=array_size and cur_row+sum_row>=1 and cur_col+sum_column<=array_size and cur_col+sum_column>=1):
        cur_row+=sum_row;
        cur_col+=sum_column;

print(cur_row,cur_col)
