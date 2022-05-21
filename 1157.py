word=input()

word=word.lower()
spelling=[0 for i in range(26)]

for i in range(len(word)):
    spelling[ord(word[i])%97]+=1  # ascii 코드에서 a~z를 0~25까지로 사상시켜 배열에 저장.

max=-1
max_index=-1
for i in range(len(spelling)):
    if(max<spelling[i]):
        max=spelling[i]
        max_index=i
        same=False
    elif(max==spelling[i]):
        same=True

if same==True:
    print('?')
else:
    print(chr(max_index+65))

