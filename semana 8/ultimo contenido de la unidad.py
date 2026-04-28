# último contenido de la unidad ahjglfshjglfshglsf
# errores controlados: try y except

#try: #intentar
    #valor = int(input("ingresa la edad 1: "))
#except Exception as e: # para todo
    #print("FAAAH U SCREWED UP, TRY AGAIN", e) #auditable

#ValueError
#a = int(input("ingresa la edad: "))

#ZeroDivisionError
#a = 10 / 0 

# ver los errores



# ver los errores

# menu 1,2,3
# solicitar uno de los números
# mostrar con consola si fallan estos números
# todo en un loop
print("[1] uno")
print("[2] dos")
print("[3] tres")

while True:
    try:
        opc = int(input("seleccione una opción: "))

        if opc == 1 or opc == 2 or opc == 3:
            break
        else:
            print("ingresa una de las opciones válidas")
    except ValueError:
        print("error, ingrese una de las opciones que se muestran")

print(opc)