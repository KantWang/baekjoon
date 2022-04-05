a = []
index = 0
max = 0
for i in range(9):
    a.append(input())
    if int(a[i]) > max:
        max = int(a[i])
        index = i + 1

print(max)
print(index)       