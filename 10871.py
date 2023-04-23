num = 0 #n개
originum = 0 #비교값
num, originum = map(int, input().split())
l = input().split()
l = list(map(int, l))
for i in range(num):
    if l[i] < originum:
        print(l[i], end = ' ')
