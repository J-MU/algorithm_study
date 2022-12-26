N,M,K=map(int,input().split())

numbers_array=list(map(int,input().split()))

numbers_array.sort(reverse=True)

first_max=numbers_array[0]
second_max=numbers_array[1]

quotient=M//(K+1)
remainder=M%(K+1)

chunk_num=first_max*K+second_max
big_number=chunk_num*quotient+first_max*remainder
print("big_number: ",big_number)

