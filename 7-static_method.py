

"""
1 - O método	estático não utiliza o parâmetro referente a	classe.
2 - O método	estático pode acessar mas não pode modificar	o estado da classe.
3-Usamos o	decorator @staticmethod para criar um método estático
"""


class Course:
    def __init__(self,name,trail):
        self.name = name
        self.trail = trail
    @staticmethod 
    def courses_trail(trail):
        if trail == "Python Fundamentos":
                courses = ["Curso Python Completo","Programação em Python do básico ao avançado", "Formação em Python"]
        elif trail == "Automação com N8N":
                courses =["N8N: Construa Agentes de IA do Zero","Curso de Automação e Agentes de IA com n8n","Curso de N8N: Automação Sem Limites, Open-Source e com IA"]
        else:
                courses = ["Definindo...."]
        return courses
print(Course.courses_trail("Automação com N8N"))