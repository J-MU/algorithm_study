array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j

    array[i],array[min_index]=array[min_index],array[i] # 파이썬에서는 이와 같은 방식으로 간단히 SWAP을 작성할 수 있다.

print(array)
