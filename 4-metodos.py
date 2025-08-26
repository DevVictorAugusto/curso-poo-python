class Filme:
    def __init__(self ,name ,yearLaunch ,includedPlan ,note ,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan =includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    def __str__(self):
        return f"Filme: {self.name}"
    def listaTecnica(self):
        print("Dados do filme")
        print(f"Nome do filme {self.name}")
        print(f"Ano de lançamento {self.yearLaunch}")
        print(f"Está Plano?  {self.includedPlan}")
        print(f"Nota {self.note}")
        print(f"Duração {self.durationMinutes}")

opoco = Filme("O poço", 2020,True,4.8, 220)
senna = Filme("Senna: O Brasileiro, O Herói, O Campeão",2010,False,4.6,180)
opoco.listaTecnica()
print("==================================================")
senna.listaTecnica()
