num = int(input())
l = []
for i in range(num):
    age, name = input().split()
    age = int(age)
    l.append((age, i, name))
l.sort()
for age, i, name in l:
    print(age, name)