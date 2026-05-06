
# crear un programa que tenga un menú y solicite la siguiente

# [1] solicitar peso
# [2] solicitar la altura
# [3] calcular el imc
# [4] salir

# probemo con float

def solicitar_peso():
    return float(input("Ingrese su peso en kg: "))

def solicitar_altura():
    return float(input("Ingrese su altura en metros: "))

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def menu():
    peso = 0
    altura = 0
    while True:
        print("\n--- Calculadora de IMC ---")
        print("1. Ingresar peso")
        print("2. Ingresar altura")
        print("3. Calcular IMC")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                peso = solicitar_peso()
                print(f"Peso registrado: {peso} kg")
            except ValueError:
                print("Error: Ingrese una opción válida (solo números).")

        elif opcion == '2':
            try:
                altura = solicitar_altura()
                print(f"Altura registrada: {altura} m")
            except ValueError:
                print("Error: Ingrese una opción válida (solo números).")

        elif opcion == '3':
            if peso == 0 or altura == 0:
                print("Por favor, ingrese peso y altura antes de calcular el IMC.")
            else: 
                imc = calcular_imc(peso, altura)
                clasificacion = clasificar_imc(imc)
                print(f"\nSu IMC es: {imc:.2f}")
                print(f"Clasificación: {clasificacion}")

        elif opcion == '4': 
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()