#Relacionamento  "é um"



class Animal():
    name = ""
    size     = ""
    color = ""

    def eat(self):
        print("Comendo ")
class Horse(Animal):
    race = ""
    def escape(self):
        print("Fuga")
class Lion(Animal):
    mane = True

    def hunt(self):
        print("Leão Caçando")

cavalo = Horse()
cavalo.name = "Bizão"
cavalo.color = "Cinza"
cavalo.size = "2 metros"

cavalo.escape()

print("##########################")

leao = Lion()
leao.name = "Zago"
leao.color = "Amarelado"
leao.size = "1.90"
leao.eat()
leao.hunt()