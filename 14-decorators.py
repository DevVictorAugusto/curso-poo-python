def my_decorator(func):
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função ")
    return wrapper

def uppercase_decorator(funcioton):
    def wrapper():
        func = funcioton()
        maker_uppercase =func.upper()
        return maker_uppercase
    return wrapper