array=[7,5,9,0,3,1,6,2,4,8];

for i in range(len(array)):
    max_index=i
    for j in range(i+1,len(array)):
        if array[max_index]<array[j]:
            max_index=j

    array[i],array[max_index]=array[max_index],array[i] # 파이썬에서는 이와 같은 방식으로 간단히 SWAP을 작성할 수 있다.

print(array)