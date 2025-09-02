class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary
    def show(self):
        print(f"Olá {self.name} , seu salario esse mes foi de {self.__salary}")

    #Método que busca dados
    def get_salaty(self):
         return self.__salary
    #Método que modifica esses dados
    def set_salary(self,salary):
         self.__salary = salary

victor = Employee("Victor", "10000")
lucas = Employee("Lucas","10000")
victor.show()   
victor.set_salary(767)   
victor.show()   
