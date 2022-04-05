x, y, w, h = [int(i) for i in input().split()]
print(min([x, h - y, w - x, y]))