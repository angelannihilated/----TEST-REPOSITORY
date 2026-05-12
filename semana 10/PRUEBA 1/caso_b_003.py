
while True:
    print("***HELADO BARRIO LITE***")
    print("Bienvenido!, este es nuestro catálogo:")
    print("[1]: Helado de Vainilla sin lactosa: $4500")
    print("[2]: Helado de Fresa sin lactosa: $5000")
    print("[3] Helado de Chocolate sin lactosa: $5500")
    print("[4] Helado de Coco sin lactosa: $5200")

    try:
        opc_menu = int(input("elija el producto que desee: "))
        if opc_menu == 1:
            print("Usted ha elegido el Helado de Vainilla sin lactosa, precio:", "$4500")
            precio = 4500
        elif opc_menu == 2:
            print("Usted ha elegido el Helado de Fresa sin lactosa, precio:", "$5000")
            precio = 5000
        elif opc_menu == 3:
            print("usted ha elejido el Helado de Chocolate sin lactosa precio:", "$5500")
            precio = 5500
        elif opc_menu == 4:
            print("usted ha elejido el Helado de Coco sin lactosa precio:", "5200")
            precio = 5200
        else:
            print("error, producto no válido... elija denuevo!")
    except ValueError:
        print("elija las opciones que están en pantalla")

    # distancias con precios y cosaghjdlaghdsfjlghsfljgh

    menu_distancia = int(input("ingrese la distancia: "))
    try:
        if menu_distancia <= 2:
            print("usted está a", menu_distancia, "km", "de la cafeteria, cuyo precio de envío es de $1500")
            print("tiempo de envío: 20 minutos")
            precio_distancia = 1500
            envio_tiempo = 20
        elif menu_distancia > 2 and menu_distancia <=5: 
            print("usted está a", menu_distancia, "km", "de la cafeteria, cuyo precio de envío es de $2500")
            print("tiempo de envío: 35 minutos")
            precio_distancia = 2500
            envio_tiempo = 35
        elif menu_distancia > 5: 
            print("usted está a", menu_distancia, "km", "de la cafeteria, cuyo precio de envío es de $4000")
            print("tiempo de envío: 50 minutos")
            precio_distancia = 4000
            envio_tiempo = 50
        else:
            print("ingrese una distancia válida.")
    except ValueError:
        print("intente denuevo.")

    except ValueError:
        print("error!, ingrese una opción valida !!")

    # sumario de los productos !

    print("***BOLETA***")
    if opc_menu == 1 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
        print("producto: Helado de Vainilla sin lactosa - $", precio)
        print("precio de envio: ", "$", precio_distancia)
        print("tiempo de envío: ", envio_tiempo, "minutos")
        print("total a pagar: ")
        print("==================================")
        suma = precio + precio_distancia
        print(suma)
        print("==================================")
    elif opc_menu == 2 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
        print("producto: Helado de Fresa sin lactosa - $", precio)
        print("precio de envio: ", "$", precio_distancia)
        print("tiempo de envio: ", envio_tiempo, "minutos")
        print("total a pagar: ")
        print("==================================")
        suma = precio + precio_distancia
        print(suma)
        print("==================================")
    elif opc_menu == 3 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
        print("producto: Helado de Chocolate sin lactosa - $", precio)
        print("precio de envio: ", "$", precio_distancia)
        print("tiempo de envio: ", envio_tiempo, "minutos")
        print("total a pagar: ")
        print("==================================")
        suma = precio + precio_distancia
        print(suma)
        print("==================================")
    elif opc_menu == 4 and menu_distancia == 2 or menu_distancia >= 2 and 5 or menu_distancia > 5:
        print("producto: Helado de Coco sin lactosa - $", precio)
        print("precio de envio: ", "$", precio_distancia)
        print("tiempo de envio: ", envio_tiempo, "minutos")
        print("total a pagar: ")
        print("==================================")
        suma = precio + precio_distancia
        print(suma)
        print("==================================")
    else:
        print("error, intente denuevo !")

    print("gracias por comprar con nosotros!, hasta luego!")