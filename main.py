import globales as g
import os 
import fun as f

def menuMain():
    b=True
    while b:
        os.system("cls")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")
        opc=g.seleccionar_opcion(3)
        if opc==1:
            f.cargarPord()
            input("presione enter para continuar")
        elif opc==2:
            os.system("cls")
            print("1 - Producto con valor más alto.")
            print("2 - Producto con valor del IVA más bajo.")
            print("3 - Promedio del valor de los productos.")
            print("4 - Media geométrica del valor de los productos.")
            opc2=g.seleccionar_opcion(4)
            if opc2==1:
                f.valorAlto()
                input("presione enter para continuar")
            if opc2==2:
                f.ivaBajo()
                input("presione enter para continuar")
            if opc2==3:
                f.mean()
                input("presione enter para continuar")
            if opc2==4:
                f.geometric_mean()
                input("presione enter para continuar")
        elif opc==3:
            print("saliendo del programa....")
            break

menuMain()
