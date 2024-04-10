from datetime import date
from especialidad import Especialidad
from medico import Medico
from paciente import Paciente
from turno import Turno

# Lista de especialidades
especialidades = [
    Especialidad("Cardiología", 1),
    Especialidad("Pediatría", 2),
]

# Lista de médicos
medicos = [
    Medico("Dr. Juan Pérez", "12345", date(2000, 1, 1)),
    Medico("Dra. María García", "67890", date(2005, 5, 5)),
]

# Asignar especialidades a cada médico
medicos[0].add_especialidad(especialidades[0])  # Dr. Juan Pérez - Cardiología
medicos[1].add_especialidad(especialidades[1])  # Dra. María García - Pediatría

# Lista de pacientes
pacientes = [
    Paciente("Ana Martínez", "11111111", "Av. Principal 123", date(1990, 3, 15)),
    Paciente("Carlos López", "22222222", "Calle Secundaria 456", date(1985, 7, 20)),
]

pacientes[0].turnos = [Turno("2024-04-07", "10:30")]

medicos[0].turnos = [
    Turno("2024-04-07", "10:00"),
    Turno("2024-04-07", "10:30"),
    Turno("2024-04-07", "11:00"),
    Turno("2024-04-07", "11:30"),
    Turno("2024-04-07", "12:00"),
    Turno("2024-04-07", "12:30"),
    Turno("2024-04-07", "13:00"),
    Turno("2024-04-07", "13:30"),
    Turno("2024-04-07", "14:00"),
    Turno("2024-04-07", "14:30"),
    Turno("2024-04-07", "15:00"),
    Turno("2024-04-07", "15:30"),
    Turno("2024-04-07", "16:00"),
    Turno("2024-04-07", "16:30"),
    Turno("2024-04-07", "17:00"),
    Turno("2024-04-07", "17:30"),
    Turno("2024-04-07", "18:00"),
    Turno("2024-04-07", "18:30"),
    Turno("2024-04-07", "19:00"),
    Turno("2024-04-07", "19:30")
]

# Definir los turnos para el segundo médico
medicos[1].turnos = [
    Turno("2024-04-07", "12:00"),
    Turno("2024-04-07", "12:30"),
    Turno("2024-04-07", "13:00"),
    Turno("2024-04-07", "13:30"),
    Turno("2024-04-07", "14:00"),
    Turno("2024-04-07", "14:30"),
    Turno("2024-04-07", "15:00"),
    Turno("2024-04-07", "15:30"),
    Turno("2024-04-07", "16:00"),
    Turno("2024-04-07", "16:30"),
    Turno("2024-04-07", "17:00"),
    Turno("2024-04-07", "17:30"),
    Turno("2024-04-07", "18:00"),
    Turno("2024-04-07", "18:30"),
    Turno("2024-04-07", "19:00"),
    Turno("2024-04-07", "19:30")
]
