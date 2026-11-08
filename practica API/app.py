from fastapi import FastAPI, Body

app: FastAPI = FastAPI()

@app.get(
    '/pj',
    description = 'Este es un endpoint que devuelve el mensaje hola',
    summary = 'aca va el titulo chidisimo del endpoint',
    name = 'Hola mundo xdddddd'
)

@app.post(
    '/Datos_Estudiante',
    description = 'En este endpoint se ingresara el nombre, apellido y cedula',
    summary = 'Estudiante')
def datos_yo(
    nombre: str = Body(...),
    apellido: str = Body(...),
    cedula: str = Body(...)
):
    return {
        "mensaje": "Datos recibidos correctamente",
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula
    }

@app.post(
    '/Promedio_Notas',
    description = 'En este endpoint se ingresara las notas del estudiante',
    summary = 'Promedio'
)

def dilon():
    
    x = 1
    y = 2
    
    print(x+2)
    
    return {
        'msj': 'hola',
        'resultado': y+2
    }