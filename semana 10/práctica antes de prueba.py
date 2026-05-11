# mostrar un menu con al menos 4 productos y sus precios
# permitir repetir la solicitud mientras el usuario no elija salir
# usar if para decidir costos de envío y tiempo de entrega según distancia
# usar try/except para validar entradas numéricas y evitar que el programa crashee si usa texto o valor inválido (bruh)

print("***PIZZERIA PIZZA NOSTRA***")
print("Bienvenido!, este es nuestro catálogo:")
print("[1]: Pizza Margarita - $8000")
print("[2]: Pepperoni - $9500")
print("[3] Cuatro Quesos - $11000")
print("[4] Napolitana - $ 10000")

try:
    opc_menu = int(input("elija la pizza que desee: "))
    if opc_menu == 1:
        print("Usted ha elegido la pizza margarita el cual da un precio de:", "$8000")
        precio = 8000
    elif opc_menu == 2:
        print("usted ha elejido la pizza Pepperoni el cual da un precio de:", "$9500")
        precio = 9500
    elif opc_menu == 3:
        print("usted ha elejido la pizza cuatro quesos cuyo precio es de:", "$11000")
        precio = 11000
    elif opc_menu == 4:
        print("usted ha elejido la pizza napolitana cuyo precio es de:", "10000")
        precio = 10000
    else:
        print("error, producto no válido... elija denuevo!")
except ValueError:
    print("elija las opciones que están en pantalla")

# distancias con precios y cosaghjdlaghdsfjlghsfljgh

menu_distancia = int(input("ingrese la distancia: "))
try:
    if menu_distancia <= 2:
        print("usted está a", menu_distancia, "km", "de la pizzería, cuyo precio de envío es de $1500")
        print("tiempo de envío: 20 minutos")
        precio_distancia = 1500
        envio_tiempo = 20
    elif menu_distancia > 2 and menu_distancia <=5: 
        print("usted está a", menu_distancia, "km", "de la pizzería, cuyo precio de envío es de $2500")
        print("tiempo de envío: 35 minutos")
        precio_distancia = 2500
        envio_tiempo = 35
    elif menu_distancia > 5: 
        print("usted está a", menu_distancia, "km", "de la pizzería, cuyo precio de envío es de $4000")
        print("tiempo de envío: 50 minutos")
        precio_distancia = 4000
        envio_tiempo = 50
    else:
        print("ingrese una distancia válida.")
except ValueError:
    print("intente denuevo.")

# sumario de los productos !

print("***BOLETA***")
if opc_menu == 1 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
    print("producto: Pizza Margarita - $", precio)
    print("precio de envio: ", "$", precio_distancia)
    print("tiempo de envío: ", envio_tiempo, "minutos")
    print("total a pagar: ")
    print("==================================")
    suma = precio + precio_distancia
    print(suma)
    print("==================================")
elif opc_menu == 2 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
    print("producto: Pepperoni - $", precio)
    print("precio de envio: ", "$", precio_distancia)
    print("tiempo de envio: ", envio_tiempo, "minutos")
    print("total a pagar: ")
    print("==================================")
    suma = precio + precio_distancia
    print(suma)
    print("==================================")
elif opc_menu == 3 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
    print("producto: Cuatro Quesos - $", precio)
    print("precio de envio: ", "$", precio_distancia)
    print("tiempo de envio: ", envio_tiempo, "minutos")
    print("total a pagar: ")
    print("==================================")
    suma = precio + precio_distancia
    print(suma)
    print("==================================")
elif opc_menu == 4 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
    print("producto: Napolitana - $", precio)
    print("precio de envio: ", "$", precio_distancia)
    print("tiempo de envio: ", envio_tiempo, "minutos")
    print("total a pagar: ")
    print("==================================")
    suma = precio + precio_distancia
    print(suma)
    print("==================================")
else:
    print("nah this ain't it vrotato i'm out of here 🥀🥀🥀")

print("gracias por comprar con nosotros!, hasta luego!")