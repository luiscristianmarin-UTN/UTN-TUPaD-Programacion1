# Trabajo Práctico integrador – Repetitivas- Condicionales y Secuenciales.
# Luis Cristian Marín


# ====================================================================
# === EJERCICIO 1 - CAJA DEL KIOSCO ===

# Nombre: solo letras, validado con .isalpha() en while
nombre = input("Ingrese nombre del cliente: ")

while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Ingrese nombre del cliente: ")


# Cantidad: entero positivo, validado con .isdigit() en while
cantidad = input("Ingrese cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero positivo, sin coma ni punto decimal.")
    cantidad = input("Ingrese cantidad de productos: ")

cantidad = int(cantidad)


total_sin_descuento = 0
total_con_descuento = 0


# Recorrer cada producto usando for
for producto in range(1, cantidad + 1):

    # Precio: entero, validado con .isdigit()
    precio = input(f"Producto {producto} - Precio: ")

    while not precio.isdigit():
        print("Error: ingrese un precio entero, sin coma ni punto decimal.")
        precio = input(f"Producto {producto} - Precio: ")

    precio = int(precio)

    # Descuento: validar S/N aceptando mayúsculas y minúsculas
    descuento = input("¿Tiene descuento? (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ").lower()

    total_sin_descuento += precio

    # Aplicar 10% de descuento cuando corresponda
    if descuento == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento


ahorro = total_sin_descuento - total_con_descuento

# La división / devuelve float; luego se muestra con 2 decimales
promedio = total_con_descuento / cantidad


print("================================")
print("       RESUMEN DE COMPRA")
print("================================")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("================================")


# ====================================================================
# === EJERCICIO 2 - ACCESO AL CAMPUS Y MENÚ SEGURO ===

# Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso_concedido = False


# Máximo 3 intentos de acceso
while intentos < 3 and not acceso_concedido:

    print("==============================")
    print(f"       INTENTO {intentos + 1}/3")
    print("==============================")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("Acceso concedido.")
    else:
        intentos += 1
        print("Error: credenciales inválidas.")


# Si falla 3 veces, bloquear
if not acceso_concedido:
    print("==============================")
    print("        CUENTA BLOQUEADA")
    print("==============================")

else:

    opcion = ""

    # Menú repetitivo hasta elegir salir
    while opcion != "4":

        print("==============================")
        print("         MENÚ DEL CAMPUS")
        print("==============================")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")

        opcion = input("Opción: ")

        # Validar que sea número
        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        # Validar que esté entre 1 y 4
        while int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")


        if opcion == "1":
            print("Estado de inscripción: Inscripto")


        elif opcion == "2":

            nueva_clave = input("Ingrese nueva clave: ")

            # La clave debe tener mínimo 6 caracteres
            while len(nueva_clave) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
                nueva_clave = input("Ingrese nueva clave: ")

            confirmacion = input("Confirme la nueva clave: ")

            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada correctamente.")
            else:
                print("Error: las claves no coinciden.")


        elif opcion == "3":
            print("¡Seguí adelante, cada práctica suma!")


        elif opcion == "4":
            print("==============================")
            print("        SESIÓN FINALIZADA")
            print("==============================")



# ====================================================================
# === EJERCICIO 3 - AGENDA DE TURNOS CON NOMBRES ===

# Turnos del lunes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Turnos del martes
martes1 = ""
martes2 = ""
martes3 = ""


# Nombre del operador: solo letras
operador = input("Ingrese nombre del operador: ")

while not operador.isalpha():
    print("Error: el nombre debe contener solo letras.")
    operador = input("Ingrese nombre del operador: ")


opcion = ""

# Menú repetitivo hasta cerrar el sistema
while opcion != "5":

    print("================================")
    print("        AGENDA DE TURNOS")
    print("================================")
    print(f"Operador: {operador}")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    # Validar opción con .isdigit() y rango 1 a 5
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: ingrese una opción válida entre 1 y 5.")
        opcion = input("Opción: ")


    # === RESERVAR TURNO ===
    if opcion == "1":

        print("1. Lunes")
        print("2. Martes")

        dia = input("Seleccione día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione día: ")

        paciente = input("Ingrese nombre del paciente: ")

        # Nombre del paciente: solo letras
        while not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")


        # Reservar turno del lunes
        if dia == "1":

            # Verificar que el paciente no esté repetido
            repetido = (
                paciente.lower() == lunes1.lower()
                or paciente.lower() == lunes2.lower()
                or paciente.lower() == lunes3.lower()
                or paciente.lower() == lunes4.lower()
            )

            if repetido:
                print("Error: el paciente ya tiene un turno el lunes.")

            # Guardar en el primer espacio libre
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado: Lunes - Turno 1.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado: Lunes - Turno 2.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado: Lunes - Turno 3.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado: Lunes - Turno 4.")

            else:
                print("No hay turnos disponibles para el lunes.")


        # Reservar turno del martes
        elif dia == "2":

            # Verificar que el paciente no esté repetido
            repetido = (
                paciente.lower() == martes1.lower()
                or paciente.lower() == martes2.lower()
                or paciente.lower() == martes3.lower()
            )

            if repetido:
                print("Error: el paciente ya tiene un turno el martes.")

            # Guardar en el primer espacio libre
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado: Martes - Turno 1.")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado: Martes - Turno 2.")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado: Martes - Turno 3.")

            else:
                print("No hay turnos disponibles para el martes.")


    # === CANCELAR TURNO ===
    elif opcion == "2":

        print("1. Lunes")
        print("2. Martes")

        dia = input("Seleccione día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione día: ")

        paciente = input("Ingrese nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: el nombre debe contener solo letras.")
            paciente = input("Ingrese nombre del paciente: ")


        # Cancelar turno del lunes
        if dia == "1":

            if paciente.lower() == lunes1.lower():
                lunes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes2.lower():
                lunes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes3.lower():
                lunes3 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == lunes4.lower():
                lunes4 = ""
                print("Turno cancelado correctamente.")

            else:
                print("El paciente no tiene turno el lunes.")


        # Cancelar turno del martes
        elif dia == "2":

            if paciente.lower() == martes1.lower():
                martes1 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == martes2.lower():
                martes2 = ""
                print("Turno cancelado correctamente.")

            elif paciente.lower() == martes3.lower():
                martes3 = ""
                print("Turno cancelado correctamente.")

            else:
                print("El paciente no tiene turno el martes.")


    # === VER AGENDA DEL DÍA ===
    elif opcion == "3":

        print("1. Lunes")
        print("2. Martes")

        dia = input("Seleccione día: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Seleccione día: ")


        if dia == "1":

            print("================================")
            print("          AGENDA LUNES")
            print("================================")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")


        elif dia == "2":

            print("================================")
            print("         AGENDA MARTES")
            print("================================")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")


    # === RESUMEN GENERAL ===
    elif opcion == "4":

        ocupados_lunes = 0
        ocupados_martes = 0

        # Contar turnos ocupados del lunes
        if lunes1 != "":
            ocupados_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1


        # Contar turnos ocupados del martes
        if martes1 != "":
            ocupados_martes += 1

        if martes2 != "":
            ocupados_martes += 1

        if martes3 != "":
            ocupados_martes += 1


        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes


        print("================================")
        print("        RESUMEN GENERAL")
        print("================================")
        print(f"Lunes - Ocupados: {ocupados_lunes}")
        print(f"Lunes - Disponibles: {disponibles_lunes}")
        print(f"Martes - Ocupados: {ocupados_martes}")
        print(f"Martes - Disponibles: {disponibles_martes}")


        # Mostrar el día con más turnos ocupados
        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")

        else:
            print("Cantidad de turnos: Empate")


    # === CERRAR SISTEMA ===
    elif opcion == "5":

        print("================================")
        print("        SISTEMA CERRADO")
        print("================================")



# ====================================================================
# === EJERCICIO 4 - ESCAPE ROOM: LA BÓVEDA ===

# Variables iniciales indicadas por la consigna
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Variables de control
racha_forzar = 0
bloqueado = False


# Nombre del agente: solo letras, validado con .isalpha() en while
nombre = input("Ingrese nombre del agente: ")

while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Ingrese nombre del agente: ")


print("================================")
print("       ESCAPE ROOM: BÓVEDA")
print("================================")
print(f"Agente: {nombre}")


# El juego continúa mientras se mantengan las condiciones
while (
    energia > 0
    and tiempo > 0
    and cerraduras_abiertas < 3
    and not bloqueado
):

    print("================================")
    print("         ESTADO ACTUAL")
    print("================================")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")

    print("================================")
    print("            ACCIONES")
    print("================================")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opción: ")

    # Validar menú con .isdigit() y rango 1 a 3
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese una opción válida entre 1 y 3.")
        opcion = input("Opción: ")


    # === OPCIÓN 1 - FORZAR CERRADURA ===
    if opcion == "1":

        # Cada intento de forzar aumenta la racha
        racha_forzar += 1

        # Costo normal de forzar
        energia -= 20
        tiempo -= 2

        # Tercer intento consecutivo: alarma y no abre cerradura
        if racha_forzar == 3:
            alarma = True
            print("¡La cerradura se trabó!")
            print("Se activó la alarma.")
            print("No se abrió ninguna cerradura.")

        else:

            # Con energía menor a 40 existe riesgo de alarma
            if energia < 40:

                riesgo = input(
                    "Riesgo de alarma. Ingrese un número entre 1 y 3: "
                )

                while (
                    not riesgo.isdigit()
                    or int(riesgo) < 1
                    or int(riesgo) > 3
                ):
                    print("Error: ingrese un número válido entre 1 y 3.")
                    riesgo = input(
                        "Riesgo de alarma. Ingrese un número entre 1 y 3: "
                    )

                if riesgo == "3":
                    alarma = True
                    print("¡Se activó la alarma!")

            # Solo abre si no se activó la alarma
            if not alarma and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

            elif alarma:
                print("No se pudo abrir la cerradura por la alarma.")


    # === OPCIÓN 2 - HACKEAR PANEL ===
    elif opcion == "2":

        # Elegir esta opción corta la racha de forzar
        racha_forzar = 0

        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")

        # El hackeo debe realizar 4 pasos usando for
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Código parcial: {codigo_parcial}")

        # Con 8 o más caracteres se abre una cerradura
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso!")
            print("Se abrió una cerradura.")
        else:
            print("Código parcial todavía incompleto.")


    # === OPCIÓN 3 - DESCANSAR ===
    elif opcion == "3":

        # Elegir esta opción corta la racha de forzar
        racha_forzar = 0

        energia += 15

        # La energía no puede superar 100
        if energia > 100:
            energia = 100

        tiempo -= 1

        # Si la alarma está activa se descuentan 10 puntos extra
        if alarma:
            energia -= 10
            print("La alarma está activa: -10 de energía extra.")

        print("Descanso realizado.")


    # Bloqueo si hay alarma y quedan 3 minutos o menos
    if (
        alarma
        and tiempo <= 3
        and cerraduras_abiertas < 3
    ):
        bloqueado = True


# === RESULTADO FINAL ===

print("================================")
print("         RESULTADO FINAL")
print("================================")

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! {nombre} abrió la bóveda.")

elif bloqueado:
    print("DERROTA: el sistema se bloqueó por la alarma.")

elif energia <= 0:
    print("DERROTA: te quedaste sin energía.")

elif tiempo <= 0:
    print("DERROTA: se terminó el tiempo.")

print("================================")



# ====================================================================
# === EJERCICIO 5 - LA ARENA DEL GLADIADOR ===

print("================================")
print("     BIENVENIDO A LA ARENA")
print("================================")

# Nombre del Gladiador: solo letras
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")


# Variables iniciales indicadas por la consigna
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True


print("================================")
print("       INICIO DEL COMBATE")
print("================================")


# El combate continúa mientras ambos tengan vida
while vida_jugador > 0 and vida_enemigo > 0:

    # === TURNO DEL GLADIADOR ===
    if turno_gladiador:

        print("================================")
        print("           TU TURNO")
        print("================================")
        print(
            f"{nombre} (HP: {vida_jugador}) "
            f"vs Enemigo (HP: {vida_enemigo}) "
            f"| Pociones: {pociones}"
        )

        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        # Validar que sea número
        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        # Validar que esté entre 1 y 3
        while int(opcion) < 1 or int(opcion) > 3:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")


        # === OPCIÓN 1 - ATAQUE PESADO ===
        if opcion == "1":

            # El daño se maneja como float
            danio_final = float(danio_ataque_pesado)

            # Si el enemigo tiene menos de 20 HP, golpe crítico
            if vida_enemigo < 20:
                danio_final = danio_ataque_pesado * 1.5
                print("¡GOLPE CRÍTICO!")

            vida_enemigo -= danio_final

            print(
                f"¡Atacaste al enemigo por "
                f"{danio_final} puntos de daño!"
            )


        # === OPCIÓN 2 - RÁFAGA VELOZ ===
        elif opcion == "2":

            print("¡Inicias una ráfaga de golpes!")

            # La ráfaga realiza 3 golpes usando for
            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")


        # === OPCIÓN 3 - CURAR ===
        elif opcion == "3":

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1

                print("Usaste una poción.")
                print("+30 puntos de vida.")

            else:
                print("¡No quedan pociones!")


        # Termina el turno del Gladiador
        turno_gladiador = False


    # === TURNO DEL ENEMIGO ===
    else:

        vida_jugador -= danio_enemigo

        print("================================")
        print("       TURNO DEL ENEMIGO")
        print("================================")
        print(
            f"¡El enemigo te atacó por "
            f"{danio_enemigo} puntos de daño!"
        )

        # Vuelve el turno al Gladiador
        turno_gladiador = True


# === FIN DEL JUEGO ===

print("================================")
print("          FIN DEL JUEGO")
print("================================")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")

else:
    print("DERROTA. Has caído en combate.")

print("================================")


