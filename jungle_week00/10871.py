n, x = [int(i) for i in input().split()]
a = input().split()
for i in a:
    if int(i) < x:
        print(int(i), end=" ")