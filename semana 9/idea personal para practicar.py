
# *** PLANNING ***
# build a system that asks for what products you can buy with the money you put in the machine
# [1] you insert the money on the machine
# [2] it shows you a list of things you can afford
# [3] you choose the product and u have it lol nothing too crazy ...i hope.

print("*** ingrese la cantidad de dinero que desea utilizar ***")
dinero = int(input("_ingrese dinero: "))
print("usted ha ingresado $", dinero)

if dinero >= 1000:
    print("[1] croissant nutella - $600")
    print("[2] snickers - $900")