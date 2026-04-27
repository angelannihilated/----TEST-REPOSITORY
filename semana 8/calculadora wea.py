while True:
    # solicite los dos números
    num1 = int(input("ingrese el 1er número: "))
    num2 = float(input("ingrese el 2do número: "))

    print("****")
    print("[1] suma")
    print("[2] resta")
    print("[3] salir")
    opc = input("ingrese la opción: ")
    
    if opc == "1":
        print("suma")
        resultado = num1 + num2
        print("el resultado de este ejercicio es: ", resultado)
    elif opc == "2":
        print("resta")
        resultado = num1 - num2
        print("el resultado de este ejercicio es: ", resultado)
    elif opc == "3":
        print("salir")
        break
    else:
        print("oe elige bien ctm no wei hijo e la perra")
    