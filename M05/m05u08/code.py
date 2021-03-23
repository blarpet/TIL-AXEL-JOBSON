lista = []
with open("testscore.txt", "r") as f:
    for number in f:
        if len(number) > 1:
            lista.append(int(number))

print(lista)
