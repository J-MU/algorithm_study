# 이것이 코딩테스트다 -나동빈저자 (Chapter6 정렬)
# p.180
# 출처: 성적이 낮은 순서로 학생 출력하기
# 08.02

array_size=int(input())
array=list()
for i in range(array_size):
    student_name,student_score=input().split()
    array.append((student_name,int(student_score)))

for i in range(array_size):
    print(array)