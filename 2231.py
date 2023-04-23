num = int(input())
a = 0
for i in range(1, num+1):
    a = str(i)
    a = list(map(int, list(a)))
    a = sum(a)
    if a + i == num:
        break
if a + i == num:
    print(i)
else:
    print("0")
