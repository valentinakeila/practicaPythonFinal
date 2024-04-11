from tipo_archivo import TipoArchivo
from carpeta import Carpeta
from archivo import Archivo

#Tanto los achivos como carpetas forman parte de la lista de "archivos" del directorio
'''
    Estructura a generar
    /Programacion1
                  /programa_analitico.pdf
    /Programacion2
                   /unidad3.txt
                   /app.py
                   /app - copia.py (eliminado)
    /Laboratorio2 (eliminado)
                 /apunte.pdf (eliminado)
'''

#inicializo lista vacía
sistema_archivos = []

#genero tipos de archivo
tipo_archivo_pdf = TipoArchivo("Microsoft Edge PDF Document", '.pdf')
tipo_archivo_txt = TipoArchivo("Python File", '.py')
tipo_archivo_py = TipoArchivo("Documento de texto", '.txt')

#genero el directorio
sistema_archivos.append(Carpeta("Programacion1")) #agrego una carpeta
sistema_archivos.append(Carpeta("Programacion2")) #agrego una carpeta
sistema_archivos.append(Carpeta("Laboratorio2")) #agrego una carpeta

programacion1 = sistema_archivos[0] #me paro en la carpeta programacion1
programacion1.add_archivo(Archivo('programa_analitico',tipo_archivo_pdf,1000)) #agrego un arhivo

programacion2 = sistema_archivos[1] #me paro en la carpeta programacion2
programacion2.add_archivo(Archivo('unidad3',tipo_archivo_txt,2000)) #agrego un arhivo
programacion2.add_archivo(Archivo('app',tipo_archivo_py,1000)) #agrego un arhivo

#Genero un archivo repetido (- copia)
copia = Archivo('app',tipo_archivo_py,1000)
programacion2.add_archivo(copia) 
#Elimino archivo copia
copia.eliminar()

laboratorio2 = sistema_archivos[2] #me paro en la carpeta Laboratorio2
laboratorio2.add_archivo(Archivo('apunte',tipo_archivo_pdf,3000)) #agrego un arhivo
laboratorio2.eliminar() # Elimino la carpeta y archivos