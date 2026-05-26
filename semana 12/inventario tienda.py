
# con arreglo
codigo = []
producto = []
precio = []

while True:
    print("***inventario::tienda***")
    print("[!][!][!][!][!][!][!][!][!][!][!]")
    print("[1] crear producto")
    print("[2] buscar producto")
    print("[3] actualizar producto")
    print("[4] eliminar producto")
    print("[5] estadisticas")
    print("[5] salir")
    print("[!][!][!][!][!][!][!][!][!][!][!]")
    print("seleccione una opción")
    opcmenu = input("[*]_> ")
    try:
        if opcmenu == 1:
            print("***CREAR PRODUCTO***")
            producto = input("agregar producto: ") # que pasa si el código existe?
            print(producto)
            codigo = input("código del producto: ")
            print(codigo)
            precio = input("ingrese el precio del producto: ")
    except:
        print("lol u fucked up")
    break
