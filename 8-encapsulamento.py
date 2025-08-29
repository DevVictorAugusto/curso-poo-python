class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def show(self):
        print(f"Olá {self.name} , seu salario esse mes foi de {self.__salary}")

ciclano = Employee("Victor", "10000")
fulano = Employee("Lucas","10000")
ciclano;__salary = 10
ciclano.show()      