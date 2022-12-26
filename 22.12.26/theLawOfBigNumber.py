N,M,K=map(int,input().split())

numbers_array=list(map(int,input().split()))

first_max=0
second_max=0

if(numbers_array[0]>numbers_array[1]):
    # 인덱스 0 이 1보다 큰경우.
    first_max=numbers_array[0]
    second_max=numbers_array[1]
else:
    # 인덱스 1 이 0보다 크거나 같은경우
    second_max=numbers_array[0]
    first_max=numbers_array[1]

print(first_max,second_max)

# 입력받은 배열중 첫번째, 두번째 큰 값을 가져옴.
for index in range(N-2):
    print(index)
    if(numbers_array[index+2]>first_max):
        second_max=first_max
        first_max=numbers_array[index+2]
    elif(numbers_array[index+2]>second_max):
        second_max=numbers_array[index+2]

print(first_max,second_max)
quotient=M//(K+1)
remainder=M%(K+1)

chunk_num=first_max*K+second_max
big_number=chunk_num*quotient+first_max*remainder
print("big_number: ",big_number)

