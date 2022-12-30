int_arr=[]
for _ in range(10):
    int_arr.append(int(input()))



remainder_set=set()

for num in int_arr:
    remainder_set.add(num%42)


print(len(remainder_set))