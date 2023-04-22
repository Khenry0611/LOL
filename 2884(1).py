h, m = input().split()
a = 0
h = int(h)
m = int(m)
a = h*60+m
a -= 45
if a//60 < 0:
    print(24 + a//60, a % 60)
else:
    print(a//60, a%60)