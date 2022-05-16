test_case_num=int(input())

for case in range(test_case_num):
    document_num, target_document= list(map(int,input().split()))

    printer_queue=list(map(int,input().split()))
    for i in range(len(printer_queue)):
        if (i == target_document):
            printer_queue[i] = [printer_queue[i], True]
        else :
            printer_queue[i]=[printer_queue[i],False]



print(printer_queue)