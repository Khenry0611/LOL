lista = []
for i in range(1,31):
    lista.append(i)
listw = []
for _ in range(28):
    listw.append(int(input()))
for i in range(28):
    if lista[i] in listw:
        a = 0
    else:
        print(lista[i])