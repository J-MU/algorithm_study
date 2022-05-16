row_column=[]
row=[]
min_values=[]
row_num,column_num=list(map(int,input().split()))

for i in range(row_num):
    row=list(map(int,input().split()))
    min_values.append(min(row))

max_value=max(min_values)
print(max_value)
# print(max_value)
# min=[]
# for i in range(row_num):
#     min.append(row[i][0])
#     for j in range(1,column_num):
#         if(min[i]>row[i][j]):
#             min[i]=row[i][j]
#
# print(min)
# final_max=0
# final_max=min[0]
# for i in range(1,row_num):
#     if final_max<min[i]:
#         final_max=min[i]
#
# print(final_max)
