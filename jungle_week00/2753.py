def isYoonYear(year):
    if year % 400 == 0:
        return 1
    elif year % 4 == 0 and year % 100 != 0:
        return 1
    else:
        return 0

get = int(input())
print(isYoonYear(get))