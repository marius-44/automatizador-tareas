from docxtpl import DocxTemplate
from datetime import date
import os
import platform


sys_op = platform.system()
usuario = ""
ruta_guardado = ""

match sys_op:
    case "Windows":
        usuario = os.environ.get("USERNAME")
        ruta_guardado = f"C:/Users/{usuario}/Desktop"
    case "Linux":
        usuario = os.environ.get("USER")
        ruta_guardado = f"/home/{usuario}/Desktop"

template_path = "portada.docx"
template = DocxTemplate(template_path)

hoy = date.today()
dia_hoy = hoy.day
mes_num_hoy = hoy.month
anio_hoy = hoy.year

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
mes_hoy = meses[mes_num_hoy - 1]


print("¡Bienvenido al automatizador de tareas!")

quitar = str(input("¿Deseas continuar con el programa?\nIngresa 'Sí' para continuar: ")).lower()

while quitar=="sí" or quitar=="si":

    matricula = str(input("Ingresa tu matrícula: "))
    materia = str(input("Ingresa el Nombre de la materia: ")).title()
    num_unidad = int(input("Ingresa el número de Unidad: "))
    titulo = str(input("Ingresa el título de tu tarea: ")).upper()
    docente = str(input("Ingresa el Nombre del docente: ")).title()
    fecha = str(f"{dia_hoy} de {mes_hoy} del {anio_hoy}")

    datos_tarea = {
        "materia":materia,
        "num_unidad":num_unidad,
        "titulo":titulo,
        "docente":docente,
        "fecha":fecha
    }

    print(f"Los datos introducidos hasta ahora son:\n{datos_tarea}")

    pregunta = str(input("¿Los datos introducidos son correctos?\nEscribe 'Sí' para confirmar: "))
    if pregunta=="sí" or pregunta=="si":
        template.render(datos_tarea)
        os.chdir(ruta_guardado)
        template.save(f"{ruta_guardado}/{matricula}_{titulo}.docx")

    quitar = input("¿Deseas continuar con el programa?\nIngresa 'sí' para continuar, o cualquier otra cosa para detener: ")
