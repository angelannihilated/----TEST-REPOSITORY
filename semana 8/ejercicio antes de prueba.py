
# preguntar si es cliente o si quiere salir ahjglsdfhgjlsfhg

print("***CHILECONMOTOR***")
print("Bienvenido devuelta!, favor elegir las siguientes opciones !")

print("[1] Ingreso cliente")
print("[2] Salir")

while True:
    try:
        opc = int(input("seleccione una opción: "))

        if opc == 1:
            print("bienvenido!, cual es su nombre?")
            nombre = (input("ingrese su nombre: "))
            print("bienvenido,", nombre, "!")

            # Elegir la comuna para descuento (!)
            print ("elija la comuna en la que se encuentra!")
            print("[1] Santiago -> 10% de descuento")
            print("[2] Estación Central -> 12% de descuento")
            print("[3] San Bernardo 8% de descuento")
            print("[4] Maipú -> 15% de descuento")
            print("[5] La Florida -> 10% de descuento")
            print("[6] Macul -> 7% de descuento")
            print("[7] La Pintana -> 20% de descuento")
            opc2 = int(input("Elija las opciones que aparecen en pantalla: "))
            if opc2 == 1:
                print("Usted ha seleccionado la comuna de Santiago!, se le aplica un descuento del 10%")
                opc2 = 0.10
            elif opc2 == 2:
                print("Usted ha seleccionado la comuna de Estación Central!, se le aplica un descuento del 12%")
                opc2 = 0.12
            elif opc2 == 3:
                print("Usted ha seleccionado la comuna de San Bernardo!, se le aplica un descuento del 8%")
                opc2 = 0.08
            elif opc2 == 4:
                print("Usted ha seleccionado la comuna de Maipú!, se le aplica un descuento del 15%")
                opc2 = 0.15 # el % que se aplica para luego calcularlo :p
            elif opc2 == 5:
                print("Usted ha seleccionado la comuna de La Florida!, se le aplica un descuento del 10%")
                opc2 = 0.10
            elif opc2 == 6:
                print("Usted ha seleccionado la comuna de Macul!, se le aplica un descuento del 7%")
                opc2 = 0.07
            elif opc2 == 7:
                print("Usted ha seleccionado la comuna de La Pintana!, se le aplica un descuento del 20%")
                opc2 = 0.20
            else:
                print("no se le aplicará el descuento al no ser de ninguna de las comunas mencionadas")
            
            print("que servicio necesita hoy?")
            print("[1] Auto: $10,000")
            print("[2] Moto: $5,000")

            opc3 = int(input("elija el servicio que necesite: "))
            if opc3 == 1:
                print("Usted eligió la opción de servicio de auto!")
                opc3 = 10000
            elif opc3 == 2:
                print("usted eligió la opción de servicio de moto!")
                opc3 = 5000
            else:
                print("opción inválida, eliga las opciones que están en pantalla")

            calculo = opc3 - (opc3 * opc2)

            print("***SUMARIO***")
            print("precio de servicio: ", opc3)
            print("porcentaje de descuento: ", opc2)
            print("total: ", "$",calculo)

            break

        elif opc == 2:
            print("Hasta luego!, vuelva pronto")
            break
        else:
            print("elija una opcion válida.")
    except ValueError:
        print("error, ingrese una de las opciones que se muestran")