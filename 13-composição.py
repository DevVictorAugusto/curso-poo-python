#{Objeto } faz parte de {Zóologico}

class Animal():
    def  __init__(self, name,categoria):
        self.name = name
        self.categoria = categoria
class Peixe(Animal):
        race = ""
        def nadar(self):
            print("Nadando")
class Papagaios(Animal):
        color = ""
        def Voar(self):
            print("Voando")
class BichoMania:
    def __init__(self):
          self.animalcatalogo = {}
    def add_animal(self,animal):
         self.animalcatalogo[animal.name] = animal.categoria
    def total_por_categoria(self,categoria):
        result = 0 
        for animal in self.animalcatalogo.values():
              if animal == categoria:
                   result += 1
        return f"No Bicho Mania temos {result} quantidade de {categoria}"

bichomania = BichoMania()
peixe = Peixe("Pirarucu","barbatanas raquídias")
print(vars(peixe))
papagaios = Papagaios("Papagaio-do-mangue","AVES")
print(vars(papagaios))

bichomania.add_animal(peixe)
bichomania.add_animal(papagaios)

print(bichomania.total_por_categoria("aves"))
print(bichomania.total_por_categoria("barbatanas raquídias"))


         





