words_num=int(input())
words=[]
temp_word=[]

for i in range(words_num):
    word=input()
    words.append(word)


cnt=0

for word in words:
    len_word=len(word)
    current_char=word[0]
    temp_word.append(current_char)
    for index in range(1,len_word):
        next_char=word[index]
        if current_char!=next_char :
            temp_word.append(next_char)
            current_char=next_char
        else:
            current_char=next_char
    # print(temp_word)
    list_size=len(temp_word)
    set_list=set(temp_word)
    set_size=len(set_list)
    # print(set_list)
    # print(temp_word)
    # print(len(set_list),len(temp_word))

    if(list_size==set_size):
        cnt+=1
    temp_word=[]

print(cnt)