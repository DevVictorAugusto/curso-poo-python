""""

Arquivos :
opção w -	write
opção a -	append
opção r	- read

"""

#name = input("Digite seu nome: \n")
 

with open("names.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)