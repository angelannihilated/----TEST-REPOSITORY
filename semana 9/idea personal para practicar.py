
# *** PLANNING ***
# build a system that asks for what products you can buy with the money you put in the machine
# [1] you insert the money on the machine
# [2] it shows you a list of things you can afford
# [3] you choose the product and u have it lol nothing too crazy ...i hope.

def solicitar_dinero():
    return float(input("ingrese efectivo: "))

def solicitar_producto():
    return float(input("elija el producto que desee: "))

def menu():
    dinero = 0
    producto = 0
    while True:
        print("\n ***MAQUINA EXPENDEDORA***")
        print("[1] ingresar efectivo")
        print("[2] elegir producto")
        print("[3] salir")
        opcion = input("seleccione una opcion: ")

        if opcion == 1:
            try:
                dinero = solicitar_dinero()
                print(f"dinero ingresado: {dinero}")
            except ValueError:
                print("Error, ingrese una cantidad válida en números")
        elif opcion == 2:
            try:
                print("***PRODUCTOS DISPONIBLES***")
                print("[1] snickers - $1000")
                print("[2] bilz y pap 200ml - $590")
                print("[3] galletas bon o bon - $900")
                producto = solicitar_producto()
            except ValueError:
                print("elija el producto que está en pantalla.")
        elif opcion == 3:
            print("cancelando compra, hasta luego!!")
            break
        else:
            print("opcion no valida, escoja las opciones que aparecen en pantalla.")



menu()
                