input()
l = list(map(int, input().split()))
num = int(input())
count = 0
for i in l:
    if i == num:
        count += 1
print(count)
print(l.count(count))