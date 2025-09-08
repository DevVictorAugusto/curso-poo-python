nomes = []

with open("dados/nomes.txt", "r", encoding= "utf-8") as file:
    for line in file :
        nomes.append(line.rstrip())

for nome in sorted(nomes):
    print(nome)