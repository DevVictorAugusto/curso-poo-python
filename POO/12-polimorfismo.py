class Phone:
    def __init__(self,brand,model_phone,price):
        self._brand = brand
        self._model_phone = model_phone
        self._price = price
    def __str__(self):
        return f"{self._brand}{self._price}"
    @staticmethod
    def make_a_call( phome_num):
        print(f"Ligando para {phome_num}")
        return self
    def discout(self):
        return self._price * 0.10
    
class SmartPhone(Phone):
    def __init__(self, brand, model_phone, price, ram, internal_memory,back_camera):
        super().__init__(brand, model_phone, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
    def discout(self):
        return  self._price * 0.15

sansung = Phone("Sangung ", "A20", 2303)
print(sansung)
print(f"Valor do {sansung._brand} {sansung._model_phone} é {sansung._price}")
print(vars(sansung))
print(sansung.discout())

iphone = Phone("Iphone","16 " , 10300)
print(iphone)
print(iphone.discout())





