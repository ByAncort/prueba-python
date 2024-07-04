import random
import math
import statistics as s
import globales as a
def cargarPord():
    productos = [
        "Cafe Americano",
        "Te Chai",
        "Croissant",
        "Jugo Naranja",
        "Panini de Pavo y Queso",
        "Pastel de Zanahoria",
        "Espresso Doble",
        "Batido de Frutas",
        "Muffin",
        "Ensalada",
        "Chocolate Caliente",
        "Tarta de Frambuesa",
        "Sandwich de Huevo",
        "Galletas de Avena",
        "Frappe de Caramelo"
        ]
    prod=[]
    id=0
    for i in productos:
        id+=1
        valor = random.randint(20, 100)*100
        iva=math.trunc(valor*0.19 )
        # print(iva)
        valores ={
                "id":id,
                "nombre": i,
                "valor": valor,
                "iva": iva
                }
        prod.append(valores)
    
    a.guardar_archivo_json("valores.json",prod)
    print("productos guardados")
    


def valorAlto():
    valores= a.leer_archivo_json("valores.json")
    val= max(valores, key=lambda x : x["valor"])
    print(f"el valor mas alto es  : {val['nombre']} ${val['valor']}")
def ivaBajo():
    valores= a.leer_archivo_json("valores.json")
    val= min(valores, key=lambda x : x["iva"])
    print("el iva mas bajo es : ",val)
def mean():
    valores= a.leer_archivo_json("valores.json")
    valor=[]
    for i in valores:
        valor.append(i["valor"])
    print("el promedio es: ",math.trunc(s.mean(valor)))
def geometric_mean():
    valores= a.leer_archivo_json("valores.json")
    valor=[]
    for i in valores:
        valor.append(i["valor"])
    print("la media geometrica es : ",math.trunc(s.geometric_mean(valor)))


# cargarPord()
# mean()
# geometric_mean()
# valorAlto()
