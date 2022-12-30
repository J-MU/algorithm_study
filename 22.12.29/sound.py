ascending=[1,2,3,4,5,6,7,8]
desacending=[8,7,6,5,4,3,2,1]

input_arr=list(map(int,input().split()))

if(input_arr==ascending):
    print("ascending")
elif(input_arr==desacending):
    print("descending")
else:
    print("mixed")