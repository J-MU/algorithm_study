list_size,money=input().split()
list_size=int(list_size)
money=int(money)

coin_list=[]
coin_count=[]


for i in range(int(list_size)):
    new_coin=int(input())
    coin_list.append(new_coin)

coin_list.sort(reverse=True)

for i in coin_list:
    coin_count.append(money//i)
    money=money%i

sum=0
for i in coin_count:
    sum+=i

print(sum)