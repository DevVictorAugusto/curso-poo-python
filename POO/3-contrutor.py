class Filme:
    def __init__(self ,name ,yearLaunch ,includedPlan ,note ,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan =includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    def __str__(self):
        return f"Filme: {self.name}"

filme = Filme("Encontro Marcado" ,1998,True, 4.8,180)
print(filme.name)
print(filme.yearLaunch)
print(filme.includedPlan)
print(filme.note)
print(filme.durationMinutes)



