
# CRUD -> create - read - update - delete

#
nombres = ["mario", "marcelo", "antonia"]
nota = [5, 4, 6]

# CREATE -> append -> 
# nombres.clear()

nombres.append("benja")
nota.append(1)
# nombres.insert(1, "inacap")
print(nombres)

# READ - leer
print(nombres[3])
print(nota[3])

# update
nota[3] = 4.0

# delete
# nombres.pop() elimina el último elemento
nombres.pop(3)
nota.pop(3)

# del nombres[3]
