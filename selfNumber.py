number_list=[]

for i in range(1,10000+1):
    number_list.append([i,False])



def selfNumberCheck(num):
    num_str=str(num)
    digit_num=len(num_str)
    sum=num

    for i in range(digit_num):
        sum+=int(num_str[i])

    if (sum > len(number_list)):
        return
    if (number_list[sum - 1][1] == True):
        return

    number_list[sum-1][1]=True
    selfNumberCheck(sum)

for i in range(1,len(number_list)):
     selfNumberCheck(i)

for i in range(0,len(number_list)):
    if number_list[i][1]==False:
        print(number_list[i][0])

