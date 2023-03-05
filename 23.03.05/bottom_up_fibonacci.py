import time
d=[0]*101

d[1]=1
d[2]=1

def fibo(n):
    for i in range(3,n+1):
        d[i]=d[i-1]+d[i-2]

    return d[n]
start = time.time()
print(fibo(30))
end = time.time()

print(f"{end - start:.5f} sec")