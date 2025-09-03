

name = input("Digite seu nome: \n")
""""

Arquivos :
opção w -	write
opção a -	append
opção r	- read

"""
#Alternativa 1
arquivo = open( "names.txt", "a")
arquivo.write(f"{name}\n")
arquivo.close()

#Alternativa 2
with open("dados/names.txt", "a") as arquivo:
    arquivo.write(f"{name}\n")
