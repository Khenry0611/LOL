h, m = input().split()
h = int(h)
m = int(m)
a = int(input())
if h == 23 and a + m >= 60:
    print(0, (h*60 + a + m) % 60)
else:
    print((h*60 + a + m)//60, (h*60 + a + m)%60)
