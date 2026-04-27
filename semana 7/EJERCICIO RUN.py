
# solicitar el run --- sin usar for

# invertir el número:
# toma el run sin puntos ni guion y escríbelo al revés (ej: 12.345.678-?) 87654321)

# 8 elevado a 2 -- 7*3 --
#multiplicar: multiplica cada dígito por la serie 2, 3, 4, 5, 6, 7 y repita (2, 3, 4 ...)
#sumar: todos los resultados
# dividir la suma por 11 - ejemplo 138:11=12 resto 6 - (11 x 12 = 132) sobran 6
# calcular diferencia: resta el resto a dv = 11 - resto

# casos especiales:
# si la resta da 11, el DV es 0
# si la resta da 10, el DV es "K"
# puede ser del 1 al 9
# (amo como todo lo de arriba son solo instrucciones y abajo con cuea son 6-7 líneas de código :sob:)
run = input("ingrese run sin digito veridicador: ")
print(run)

#calcular = int(run[-1]) * 2 + int(run[-2]) * 3
calcular = int(run[-1]) * 2 + int(run[-2]) * 3 + int(run[-3]) * 4 + int(run[-4]) * 5 + int(run[-5]) * 6 + int(run[-6]) * 7 + int(run[-7]) * 2 + int(run[-8]) * 3
resto = calcular % 11

dv = 11 - resto

print("tu DÍGITO VERIFICADOR ES: ", dv)
