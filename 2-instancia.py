#Aula sobre instancia

class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

movie = Movie()
movie.name = "Safada digital"
movie.yearLaunch = 2025
movie.includedPlan = True
movie.note = 3.5
movie.durationMinutes = 90

print("Info Do Filme ")
print(f"Nome do Filme:{movie.name} \n Foi lançado em {movie.yearLaunch} \n Está no seu plano? {movie.includedPlan}")
print(f"Nota dele é de  {movie.note} \n Duração {movie.durationMinutes}")