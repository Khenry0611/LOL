n, m, k = map(int, input().split())
numlist = [] #정리한 값
inputlist = [] #입력한 값
for i in range(n):
    numlist.append(0)
for i in range(k):
    inputlist.append(tuple(input().split()))
for i in range(k):
    for j in range(m):
        for q in range(n):
            if int(inputlist[i][j]) - 1 == q:
                numlist[q] = numlist[q] + 1
for i in range(n):
    if numlist[i] != 0:
        print(f"{i + 1} {numlist[i]}")