
class Console:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls,string):
        import re
        item = re.findall("é \w*",string)
        name = item[0][2:]
        price = item [1][2:]
        return cls(name, int(price))
ps4 = Console.from_text("Meu video game é o PS4 e o precço é 5030")
xbox = Console.from_text("Meu video game é o XBOX e o precço é 3500")

print(ps4.__dict__)
print(xbox.__dict__)