str1 = input()
str2 = input()
num1 = int(str1)
num2 = int(str2)

sol = []
sol.append(num1 * (num2 % 10))
sol.append(num1 * ((num2 % 100) // 10))
sol.append(num1 * (num2 // 100))
sol.append(num1 * num2)

for i in sol:
    print(i)