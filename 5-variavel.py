class Filme:
    platform = "Rede Canais"
    def __init__(self ,name ,yearLaunch ,includedPlan ,note ,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan =includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    def __str__(self):
        return f"Filme: {self.name}"
    def listaTecnica(self):
        print(f"Plataformas:{Filme.platform}")
        print("Dados do filme")
        print(f"Nome do filme {self.name}")
        print(f"Ano de lançamento {self.yearLaunch}")
        print(f"Está Plano?  {self.includedPlan}")
        print(f"Nota {self.note}")
        print(f"Duração {self.durationMinutes}")


surfitinha = Filme( "Surfistinha",2014,False,3.8,165)
print(surfitinha.listaTecnica())