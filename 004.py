N, M = map(int, input().split())
lista = []
time = 0
zerocount = 0
for i in range(N):
    lista.append(int(input()))
while 1:
    time += 1
    if lista[0] > lista[1]:
        lista[0] += 1
    for i in range(N-2):
        if lista[i + 1] > lista[i] and lista[i + 1] > lista[i + 2]:
            lista[i + 1] += 1
    if lista[N-1] > lista[N - 2]:
        lista[N - 1] += 1
    for i in range(N):
        if lista[i] >= M:
            lista[i] = 0
        if lista[i] == 0:
            zerocount += 1
    if zerocount == N:
        break
    if time >= 50:
        time = -1
        break
    zerocount = 0
print(time)