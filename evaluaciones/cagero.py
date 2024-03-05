import time

# Estructuras de datos
usuarios = []
movimientos = []

# Funciones
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    clave = input("Ingrese su clave: ")
    saldo = float(input("Ingrese su saldo inicial: "))
    usuarios.append({"nombre": nombre, "clave": clave, "saldo": saldo})
    print("Usuario registrado correctamente.")

def ingresar():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        for usuario_registrado in usuarios:
            if usuario_registrado["nombre"] == usuario and usuario_registrado["clave"] == clave:
                return usuario_registrado
        intentos += 1
        print(f"Intentos fallidos: {intentos}/3")
        if intentos == 3:
            print("Cuenta bloqueada por 24 horas, comunícate con tu banco.")
            time.sleep(24 * 60 * 60)
    return None

def consultar_saldo(usuario):
    print(f"Saldo actual: ${usuario['saldo']}")

def retirar(usuario):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto > usuario['saldo']:
        print("El monto a retirar no puede ser mayor al saldo de la cuenta.")
    else:
        usuario['saldo'] -= monto
        movimientos.append({"tipo": "Retiro", "monto": monto, "fecha": time.strftime("%d/%m/%Y %H:%M:%S")})
        print(f"Saldo actualizado: ${usuario['saldo']}")

def consignar(usuario):
    monto = float(input("Ingrese el monto a consignar: "))
    if monto < 0:
        print("No se pueden ingresar datos negativos.")
    else:
        usuario['saldo'] += monto
        movimientos.append({"tipo": "Consignación", "monto": monto, "fecha": time.strftime("%d/%m/%Y %H:%M:%S")})
        print(f"Saldo actualizado: ${usuario['saldo']}")

def cambiar_clave(usuario):
    clave_nueva = input("Ingrese su nueva clave: ")
    usuario['clave'] = clave_nueva
    print("Clave cambiada correctamente.")

def consultar_movimientos():
    for movimiento in movimientos:
        print(f"{movimiento['tipo']} de ${movimiento['monto']} el {movimiento['fecha']}")

# Menú
while True:
    print("\n*********************************************\n"
          "*               Menú de opciones             *\n"
          "*                                           *\n"
          "*  1. Registrar usuario                     *\n"
          "*  2. Ingresar                              *\n"
          "*  3. Consultar saldo                       *\n"
          "*  4. Retirar                               *\n"
          "*  5. Consignar                             *\n"
          "*  6. Cambiar clave                         *\n"
          "*  7. Consultar movimientos                 *\n"
          "*  8. Salir                                 *\n"
          "*********************************************")

    opcion = int(input("Ingrese la opción deseada: "))
    if opcion == 1:
        registrar_usuario()
    elif opcion == 2:
        usuario = ingresar()
        if usuario is not None:
            print(f"Bienvenido, {usuario['nombre']}.")
    elif opcion == 3:
        usuario = ingresar()
        if usuario is not None:
            consultar_saldo(usuario)
    elif opcion == 4:
        usuario = ingresar()
        if usuario is not None:
            retirar(usuario)
    elif opcion == 5:
        usuario = ingresar()
        if usuario is not None:
            consignar(usuario)
    elif opcion == 6:
        usuario = ingresar()
        if usuario is not None:
            cambiar_clave(usuario)
    elif opcion == 7:
        consultar_movimientos()
    elif opcion == 8:
        break
    else:
        print("Opción inválida.")