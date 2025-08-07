import requests

def trivia_fetch(numero):
    try:
        numero=numero.replace(" ","")
        respuesta=requests.get(f"http://numbersapi.com/{numero}?json")
        datos=respuesta.json()
        texto=datos["text"]
        mensaje=f"El dato curioso es: {texto}"
        print(mensaje)
    except:
        print("No se encontro lo que deseabas saber. :c")

def decision(opcion):
    opcion=opcion.replace(" ","")
    while opcion not in ["si","sí","no"]:
        print("Respuesta no válida.")
        opcion=input("¿Quieres hacer otra consulta? ").lower()
    return opcion

opcion="si"
print("Datos curiosos")
while opcion in ["si","sí"]:
    numero=input("¿De que número deseas saber el dato curioso? ")
    trivia_fetch(numero)
    pregunta=input("¿Quieres hacer otra consulta? ").lower()
    opcion=decision(pregunta)
print("Gracias por usar nuestra aplicación.")