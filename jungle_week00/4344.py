def returnAverage(list):
    sum = 0
    for i in list:
        sum += int(i)
    
    return sum / len(list)

def aboveAverageRate():
    stu_list = input().split()
    stu_num = int(stu_list.pop(0))
    
    stu_good_num = 0 # 평균 이상 학생 수
    avr = returnAverage(stu_list)

    for i in stu_list:
        if float(i) > avr:
            stu_good_num += 1

    print(f'{stu_good_num / stu_num * 100:.3f}%')

num = int(input())
for i in range(num):
    aboveAverageRate()