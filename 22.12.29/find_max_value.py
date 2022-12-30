int_array=[]
for i in range(9):
    int_array.append(int(input()))
max_value=max(int_array)
index=int_array.index(max_value)
print(max_value)
print(index+1)