A=int(input())
B=int(input())
C=int(input())

product_number=A*B*C
product_str=str(product_number)

digit_count=[0 for i in range(10)]


for i in range(len(product_str)):
    digit_count[int(product_str[i])]+=1

for i in range(len(digit_count)):
    print(digit_count[i])

