
# *** PLANNING ***
# build a system that asks for what products you can buy with the money you put in the machine
# [1] you insert the money on the machine
# [2] it shows you a list of things you can afford
# [3] you choose the product and u have it lol nothing too crazy ...i hope.

def solicitar_dinero():
    return float(input("ingrese efectivo: "))

def menu():
    dinero = 0
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

menu()
                