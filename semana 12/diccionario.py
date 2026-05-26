
# diccionario - dic

pokemon = ["pichu(la)", "corxea champuru", "tepicalacola", "ozzy osbourne", "abuela wako"]
vidas = [100, 60, 120, 600, 10002]

for p in pokemon:
    print(p) # pichu tiene 100 de vida

# i seria la posicion
for i in range(len(pokemon)):
    print(pokemon[i])
    print(vidas[i])
    print(pokemon[i] + " tiene " + str(vidas[i]) + " de vida ")
    print(f" {pokemon [i]} tiene {vidas[i]} de vidas")

posicion = 0
for p in pokemon:
    print(p)
    print(vidas[posicion])
    posicion = posicion + 1

#
for key, value in enumerate(pokemon):
    print(f"{key} ---> {value} : de {vidas[key]} vidas")
    # print(vidas[key])
