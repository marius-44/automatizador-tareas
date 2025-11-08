from docxtpl import DocxTemplate
from datetime import date

template_path = "portada.docx"
template = DocxTemplate(template_path)

hoy = date.today()
dia_hoy = hoy.day
mes_num_hoy = hoy.month
anio_hoy = hoy.year

mes_hoy = ""
match mes_num_hoy:
    case 1:
        mes_hoy = "enero"
    case 2:
        mes_hoy = "febrero"
    case 3:
        mes_hoy = "marzo"
    case 4:
        mes_hoy = "abril"
    case 5:
        mes_hoy = "mayo"
    case 6:
        mes_hoy = "junio"
    case 7:
        mes_hoy = "julio"
    case 8:
        mes_hoy = "agosto"
    case 9:
        mes_hoy = "septiembre"
    case 10:
        mes_hoy = "octubre"
    case 11:
        mes_hoy = "noviembre"
    case 12:
        mes_hoy = "diciembre"

print("¡Bienvenido al automatizador de tareas!")

quitar = str(input("¿Deseas continuar con el programa?\nIngresa 'sí' para continuar: ")).lower()

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
        template.save(f"{matricula}_{titulo}.docx")

    quitar = input("¿Deseas continuar con el programa?\nIngresa 'sí' para continuar, o cualquier otra cosa para detener: ")
