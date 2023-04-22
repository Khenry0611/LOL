n, m = map(int, input().split())
l = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        l[x] = k
for i in range(1, n+1):
    print(l[i], end = ' ')
#print(*l[1:])
#print(l[1],l[2],l[3],l[4],l[5])