import math
import time

d=[0]*100

def fibo(x):
    if x==1 or x==2:
        return 1

    if d[x] !=0:
        return d[x]

    d[x]=fibo(x-1)+fibo(x-2)

    return d[x]

def fibo2(x):
    global count
    count+=1
    print(count)
    if x==1 or x==2:
        return 1

    return fibo2(x-1)+fibo2(x-2)

count=0

start = time.time()
print(fibo(99))
end = time.time()
print(f"{end - start:.5f} sec")

start = time.time()
print(fibo2(99))
end = time.time()
print(f"{end - start:.5f} sec")
