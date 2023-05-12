# Importamos el módulo time
import time

# Función para el temporizador
def timer():
    # Pedimos al usuario que ingrese los minutos y segundos
    minutes = int(input("Ingresa los minutos: "))
    seconds = int(input("Ingresa los segundos: "))
    # Calculamos el tiempo total en segundos
    time_in_seconds = minutes*60 + seconds
    # Mientras queden segundos por contar, seguimos contando
    while time_in_seconds > 0:
        # Mostramos el tiempo restante en formato mm:ss
        print(f"Tiempo restante: {time_in_seconds//60:02d}:{time_in_seconds%60:02d}")
        # Esperamos un segundo
        time.sleep(1)
        # Restamos un segundo al tiempo total en segundos
        time_in_seconds -= 1
    # Mostramos un mensaje cuando se acabe el tiempo
    print("¡Tiempo acabado!")

# Función para la cuenta regresiva
def countdown():
    # Pedimos al usuario que ingrese los segundos
    seconds = int(input("Ingresa los segundos: "))
    # Mientras queden segundos por contar, seguimos contando
    while seconds > 0:
        # Mostramos el tiempo restante en formato mm:ss
        print(f"Tiempo restante: {seconds//60:02d}:{seconds%60:02d}")
        # Esperamos un segundo
        time.sleep(1)
        # Restamos un segundo al tiempo total en segundos
        seconds -= 1
    # Mostramos un mensaje cuando se acabe el tiempo
    print("¡Cuenta regresiva acabada!")

# Ciclo principal del programa
while True:
    # Mostramos el menú de opciones
    print("------ Temporizador y Reloj de Cuenta Regresiva ------")
    print("1. Temporizador")
    print("2. Cuenta Regresiva")
    print("3. Salir")
    # Pedimos al usuario que seleccione una opción
    option = int(input("Ingresa el número de opción: "))
    # Dependiendo de la opción seleccionada, llamamos a la función correspondiente
    if option == 1:
        timer()
    elif option == 2:
        countdown()
    elif option == 3:
        # Salimos del programa si el usuario selecciona la opción de salir
        print("¡Hasta luego!")
        break
    else:
        # Mostramos un mensaje de error si el usuario ingresa una opción inválida
        print("Opción inválida.")
