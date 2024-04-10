from datos import *



def reservarTurno():
    for especialidad in especialidades:
        print(f"{especialidad.nombre}-{especialidad.codigo}" )

    codigo_especialidad = int(input("Ingrese el código de la especialidad: "))

    especialidad_valida = False
    for especialidad in especialidades:
        if codigo_especialidad == especialidad.codigo:
            especialidad_valida = True
            for medico in medicos:
                print(f"{medico.nombre_apellido} - {medico.matricula}")
            medicoElegido = input("Elija ingrese matricula")
            for medico in medicos:
                if medicoElegido == medico.matricula:
                    print("Turnos disponibles para el médico", medico.nombre_apellido)
                    for i, turno in enumerate(medico.turnos):
                        print(f"{i + 1}Fecha: {turno.fecha}, Hora: {turno.hora}")
                    turnoElegido = int(input("Elija turno"))
                    eleccionTurno = medico.turnos[turnoElegido - 1]
                    if eleccionTurno.estado == "RESERVADO":
                        print("El turno seleccionado ya está reservado.")
                    else:
                        nombre_paciente = input("Ingrese el nombre del paciente: ")
                        documento_paciente = input("Ingrese el número de documento del paciente: ")
                        direccion_paciente = input("Ingrese la dirección del paciente: ")
                        fecha_nacimiento_paciente = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")

                        paciente = Paciente(nombre_paciente, documento_paciente, direccion_paciente, fecha_nacimiento_paciente)

            # Asignar el paciente al turno seleccionado
                        eleccionTurno.paciente = paciente
                        eleccionTurno.estado = "RESERVADO"
                        eleccionTurno.autorizado = False
                        print("¡Turno reservado con éxito!")
                    break

            else:  
                print("No se encontró al médico con la matrícula ingresada.")
            break

            break
        else:
            print("no valido")
        

def cancelarTurno():
    nro_documento = input("Ingrese el número de documento del paciente: ")

    paciente_encontrado = False
    for paciente in pacientes:
        if paciente.nro_documento == nro_documento:
            paciente_encontrado = True
            print("Turnos futuros del paciente:")
          





while True:
    print("1- Reservar turno\n")
    print("2-Cancelar turno\n")
    print("3-Ingresar paciente\n")
    opt = input("Ingrese la opción seleccionada: ")
    if opt == "1":
        reservarTurno()
        continue
    if opt == "2":
        cancelarTurno()
        continue
    if opt == "3":
        
       
        continue
    if opt == "4":
        print("Saludos.")
        break
    else:
        print("Ingrese una opcion valida.")