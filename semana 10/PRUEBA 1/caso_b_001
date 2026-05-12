# caso 1 :: control de velocidad de vehículos // validador de patente [!]

# pedir el nombre del conductor
def nombre_conductor():
    return float(input("ingrese el nombre del conductor: "))

# pedir la patente del vehículo
def patente_vehiculo():
    return float(input("ingrese la patente del vehiculo: "))

# pedir la velocidad del vehículo del auto
def velocidad_conductor():
    return int(input("ingrese la velocidad del conductor: "))

def patente_autorobado():
    patente_autorobado = "AB-CD-23" and "GB-TF-31"

# código principal con el menú para registrar :)!

def menu():
    
    velocidad_conductor = 0
    while True:
        try:
            print("***REGISTRO DE VELOCIDAD***")
            print("[1] registrar patente")
            print("[2] verificar patente con orden de robo")
            print("[3] registrar velocidad de vehículo")
            print("[4] nombre del conductor")
            print("[5] sumario")
            print("[6] salir de la plataforma")

            opc = int(input("elija la operación que va a utilizar: "))
            if opc == 1:
                try:
                    print("registre la patente que está controlando")
                    patente_vehiculo = input("ingrese la patente: ")
                    print(f"patente registrada: ", patente_vehiculo)
                
                except ValueError:
                    print("error, patente ingresada de forma incorrecta.")
                    print("ejemplo: CX-JK-22")
            elif opc == 2:
                try:
                    print("***PATENTES CON ORDEN DE ROBO***")
                    patente_autorobado = print("AB-CD-23", "GB-TF-31")
                except ValueError:
                    print("ERROR")
            elif opc == 3:
                try:
                    velocidad_conductor = int(input("ingrese la velocidad del conductor: "))
                    if velocidad_conductor <= 100:
                        print("el conductor está manejando de forma segura.")
                    elif velocidad_conductor > 100:
                        print("el conductor está manejando de forma peligrosa [MULTA]")
                except ValueError:
                    print("ERROR, INTENTE DENUEVO")
            elif opc == 4:
                try:
                    nombre_conductor = input("ingrese el nombre del conductor: ")
                    print("nombre del conductor: ", nombre_conductor)
                except ValueError:
                    print("ERROR, ingrese el nombre denuevo.")
            elif opc == 5:
                print("***SUMARIO***")
                print("nombre del conductor: ", nombre_conductor)
                print("patente vehicular: ", patente_vehiculo or patente_autorobado)
                print("velocidad vehículo: ", velocidad_conductor)
            elif opc == 6:
                print("saliendo del programa...")
                break
        except ValueError:
            print("intente denuevo !")
menu()