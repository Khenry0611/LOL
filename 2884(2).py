h, m = input().split()
h = int(h)
m = int(m)

if 45 <= m:
    print(h, m-45)
else:
    if h ==  0:
        print(23, 15 + m )
    else:
        print(h - 1, 15 + m)