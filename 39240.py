l = []
maximum = 0
x = 0
y = 0
for i in range(9):
    t = list(map(int, input().split))
    l.append(t)
for i in range(9):
    for j in range(9):
        if maximum < l[i][j]:
            maximum = l[i][j]
            x = i
            y = j
print(maximum)
print(x+1,y+1)
