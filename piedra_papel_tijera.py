import random  # Importamos el módulo random (modulo de la biblioteca estándar de Python) para generar opciones aleatorias

def generar_opcion_maquina():
    """Genera una opción aleatoria para la máquina (piedra, papel o tijera)."""
    opciones = ['piedra', 'papel', 'tijera']  # Lista de opciones posibles
    return random.choice(opciones)  # Retorna una opción aleatoria de la lista

def jugar():
    """Solicita la opción del usuario y determina el resultado del juego."""
    opciones_usuario = ['piedra', 'papel', 'tijera']  # Opciones válidas para el usuario
    
    # Solicitar al usuario que elija una opción
    usuario = input("Elige: piedra, papel o tijera: ").lower()  # Convertimos la entrada a minúsculas
    
    # Verificamos si la opción del usuario es válida
    if usuario not in opciones_usuario:
        print("Opción inválida. Por favor elige piedra, papel o tijera.")  # Mensaje de error si la opción no es válida
        return  # Salimos de la función si la opción es inválida
    
    # Generar la opción de la máquina
    maquina = generar_opcion_maquina()  # Llamamos a la función que genera la opción de la máquina
    print(f"La máquina eligió: {maquina}")  # Mostramos la elección de la máquina

    # Determinar el resultado del juego
    if usuario == maquina:
        print("¡Es un empate!")  # Si ambas elecciones son iguales, es un empate
    elif (usuario == 'piedra' and maquina == 'tijera') or (usuario == 'papel' and maquina == 'piedra') or (usuario == 'tijera' and maquina == 'papel'):
        print("¡Ganaste!")  # Usuario gana si su opción vence a la de la máquina
    else:
        print("¡Perdiste!")  # En caso contrario, el usuario pierde

# Llamar a la función jugar para iniciar el juego si este archivo es ejecutado directamente
if __name__ == "__main__":
    jugar()  # Ejecutamos la función jugar