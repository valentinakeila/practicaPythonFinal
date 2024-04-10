from profesional import *
from concurso import *


profesionales = [Profesional("Juan", "Perez", "1111")]

titulos = [
    Titulo("Ingeniero Mecánico","Universidad Tecnologica Nacional"),
    Titulo("Contador Público Nacional","Universidad Nacional de Rosario"),
    Titulo("Ingeniería Civil Mecanica", "UNR")
]

concursos = [
    Concurso("Maestria en Ciencia de los Materiales",date(2024,4,2), date(2024,4,9)),
    Concurso("Doctorado en Finanzas",date(2024,3,28), date(2024,3,29))
]

#agrego titulos al aspirante
profesionales[0].add_titulos(titulos[0])

#agrego titulos de grado requeridos a cada carrera de postgrado
concursos[0].add_titulo_requerido(titulos[0]) 
concursos[0].add_titulo_requerido(titulos[2])
concursos[1].add_titulo_requerido(titulos[1])

#genero una inscripcion
concursos[0].add_inscripcion(profesionales[0])


