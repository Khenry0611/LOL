n = int(input())
l = []
for _ in range(n):
    a, b = map(int, input().split())
    l.append((a, b))
l.sort(key = lambda a:[a[1], a[0]] )
for a,b in l:
    print(a, b)