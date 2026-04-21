# # preguntar por el nombre
# calcular cuantas a, e, i, o, u
# calcular el total de vocales uso

# for n in range(10)
nombre = "DANIIIIEEEEEElLllL"
nombre = nombre.lower()
# print(nombre[0])

cont_e = 0
cont_a = 0
for letra in nombre:
    # iteracion -> bloque de codigo -> contexto del for
    if letra == 'e':
        cont_e = cont_e + 1
    print(letra)
    if letra == 'a':
        cont_a = cont_a + 1
        print(letra)

print(f"el total de E es {cont_e}")
print(f"el total de A es {cont_a}")
