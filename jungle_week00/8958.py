# 등차수열의 합
def arithSum(number):
    sum = 0
    for i in range(number):
        sum += i + 1
    return sum 

num = int(input())
str = []
ans = 0