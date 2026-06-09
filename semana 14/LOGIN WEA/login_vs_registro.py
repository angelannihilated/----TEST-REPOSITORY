#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv, os, sys, hashlib

CSV_FILE = "usuarios.csv"


# ------------------------------------------------------------
#  CSV HELPERS
# ------------------------------------------------------------

def leer_csv() -> list[dict]:
    """Devuelve lista de dicts con id, name, username, password."""
    if not os.path.isfile(CSV_FILE):
        return []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def guardar_csv(lst: list[dict]):
    """Sobrescribe el CSV con la lista dada."""
    fieldnames = ["id", "name", "username", "password"]
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(lst)


def siguiente_id() -> int:
    usuarios = leer_csv()
    if not usuarios:
        return 1
    return max(int(u["id"]) for u in usuarios) + 1


# ------------------------------------------------------------
#  UTILIDADES
# ------------------------------------------------------------

def nombre_existe(nombre: str) -> bool:
    return any(u["name"].lower() == nombre.lower() for u in leer_csv())


def username_existe(username: str) -> bool:
    return any(u["username"].lower() == username.lower() for u in leer_csv())


def hashear(pwd: str) -> str:
    return hashlib.sha256(pwd.encode()).hexdigest()


# ------------------------------------------------------------
#  INICIO DE SESIÓN
# ------------------------------------------------------------

def iniciar_sesion():
    print("\n=== Iniciar Sesión ===")
    username = input("Username: ").strip()
    pwd      = input("Password: ").strip()
    pwd_hash = hashear(pwd)

    for u in leer_csv():
        if u["username"].lower() == username.lower() and u["password"] == pwd_hash:
            print(f"\nWelcome, {u['name']}!")
            salir()

    print("\nCredenciales inválidas. Intenta de nuevo o regístrate.")


# ------------------------------------------------------------
#  REGISTRO
# ------------------------------------------------------------

def registrar():
    print("\n=== Registro de nuevo usuario ===")

    nombre = input("Nombre: ").strip()
    if nombre_existe(nombre):
        print(f"Ya existe un usuario con el nombre '{nombre}'.")
        return

    username = input("Username: ").strip()
    while username_existe(username):
        print("Ese username ya está en uso.")
        username = input("Elige otro username: ").strip()

    pwd = input("Password: ").strip()

    nuevo = {
        "id":       siguiente_id(),
        "name":     nombre,
        "username": username,
        "password": hashear(pwd),
    }

    usuarios = leer_csv()
    usuarios.append(nuevo)
    guardar_csv(usuarios)
    print("Registro completado. ¡Ya puedes iniciar sesión!")


# ------------------------------------------------------------
#  SALIR [99]
# ------------------------------------------------------------

def salir():
    sys.exit("\n[99] Sesión cerrada. ¡Hasta luego!")


# ------------------------------------------------------------
#  MENÚ PRINCIPAL
# ------------------------------------------------------------

def main_menu():
    while True:
        print("\n╔══════════════════════════╗")
        print("║   BIENVENIDO AL SISTEMA  ║")
        print("╠══════════════════════════╣")
        print("║ 1) Iniciar sesión        ║")
        print("║ 2) Registro              ║")
        print("║ q) Salir                 ║")
        print("╚══════════════════════════╝")

        opcion = input(">>> ").strip().lower()

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar()
        elif opcion == "q":
            salir()
        else:
            print("Opción no válida. Prueba de nuevo.")


# ------------------------------------------------------------
#  ENTRADA
# ------------------------------------------------------------

if __name__ == "__main__":
    main_menu()