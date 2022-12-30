count=int(input())



for i in range(count):
    continious_count = 0
    score = 0
    score_array = list(input())
    for answer in score_array:
        if(answer=='O'):
            continious_count=continious_count+1
            score=score+continious_count
        else:
            continious_count=0
    print(score)
