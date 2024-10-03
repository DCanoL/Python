import random  # Importa el módulo random para generar opciones aleatorias
import os  # Importa el módulo os para manejar operaciones del sistema operativo

# Archivo para almacenar los usuarios
archivo_usuarios = 'usuarios.txt'

# Cargar usuarios desde el archivo de texto
def cargar_usuarios():
    """Carga los usuarios desde el archivo de texto y los almacena en un diccionario."""
    usuarios = {}  # Inicializa un diccionario vacío para los usuarios
    if os.path.exists(archivo_usuarios):  # Verifica si el archivo existe
        with open(archivo_usuarios, 'r') as f:  # Abre el archivo en modo lectura
            for line in f:  # Itera sobre cada línea del archivo
                # Divide la línea en partes y las asigna a variables
                nombre_usuario, correo, contrasena, victorias = line.strip().split(',')
                # Agrega los datos del usuario al diccionario
                usuarios[nombre_usuario] = {
                    'correo': correo,
                    'contrasena': contrasena,
                    'victorias': int(victorias),  # Convierte victorias a entero
                    'nombre': nombre_usuario
                }
    return usuarios  # Devuelve el diccionario de usuarios

# Guardar usuarios en el archivo de texto
def guardar_usuarios():
    """Guarda los datos de los usuarios en el archivo de texto."""
    with open(archivo_usuarios, 'w') as f:  # Abre el archivo en modo escritura
        for usuario, datos in usuarios.items():  # Itera sobre el diccionario de usuarios
            # Escribe los datos del usuario en una línea
            f.write(f"{usuario},{datos['correo']},{datos['contrasena']},{datos['victorias']}\n")

# Diccionario para almacenar los usuarios y sus datos
usuarios = cargar_usuarios()  # Carga los usuarios al inicio del programa

def generar_opcion_maquina():
    """Genera una opción aleatoria para la máquina (piedra, papel o tijera)."""
    opciones = ['piedra', 'papel', 'tijera']  # Lista de opciones posibles
    return random.choice(opciones)  # Retorna una opción aleatoria

def registrar_usuario():
    """Registra un nuevo usuario en el sistema."""
    correo = input("Ingresa tu correo: ")  # Solicita el correo del usuario
    nombre_usuario = input("Elige un nombre de usuario: ")  # Solicita el nombre de usuario
    contrasena = input("Elige una contraseña: ")  # Solicita la contraseña
    
    if nombre_usuario in usuarios:  # Verifica si el nombre de usuario ya existe
        print("El nombre de usuario ya está en uso. Intenta con otro.")  # Mensaje de error
        return None  # Sale de la función si el nombre está en uso
    
    # Agrega el nuevo usuario al diccionario
    usuarios[nombre_usuario] = {
        'correo': correo,
        'contrasena': contrasena,
        'victorias': 0,  # Inicializa las victorias en 0
        'nombre': nombre_usuario
    }
    print(f"Usuario {nombre_usuario} registrado con éxito.")  # Mensaje de éxito
    guardar_usuarios()  # Guarda los cambios después de registrar
    return nombre_usuario  # Retorna el nombre de usuario

def login_usuario():
    """Inicia sesión de un usuario registrado."""
    nombre_usuario = input("Ingresa tu nombre de usuario: ")  # Solicita el nombre de usuario
    contrasena = input("Ingresa tu contraseña: ")  # Solicita la contraseña
    
    # Verifica si el usuario existe y si la contraseña es correcta
    if nombre_usuario in usuarios and usuarios[nombre_usuario]['contrasena'] == contrasena:
        print(f"Bienvenido, {usuarios[nombre_usuario]['nombre']}!")  # Mensaje de bienvenida
        return nombre_usuario  # Retorna el nombre de usuario
    else:
        print("Credenciales incorrectas. Intenta nuevamente.")  # Mensaje de error
        return None  # Retorna None si las credenciales son incorrectas

def jugar(usuario):
    """Solicita la opción del usuario y determina el resultado del juego."""
    opciones_usuario = ['piedra', 'papel', 'tijera']  # Opciones válidas para el usuario
    victorias_usuario = 0  # Inicializa las victorias del usuario
    victorias_maquina = 0  # Inicializa las victorias de la máquina
    
    # Bucle que continúa hasta que uno de los dos llegue a 3 victorias
    while victorias_usuario < 3 and victorias_maquina < 3:
        usuario_opcion = input("Elige: piedra, papel o tijera: ").lower()  # Solicita la opción del usuario
        
        if usuario_opcion not in opciones_usuario:  # Verifica si la opción es válida
            print("Opción inválida. Por favor elige piedra, papel o tijera.")  # Mensaje de error
            continue  # Salta a la siguiente iteración del bucle
        
        maquina_opcion = generar_opcion_maquina()  # Genera la opción de la máquina
        print(f"La máquina eligió: {maquina_opcion}")  # Muestra la opción de la máquina

        # Determina el resultado del juego
        if usuario_opcion == maquina_opcion:
            print("¡Es un empate!")  # Empate
        elif (usuario_opcion == 'piedra' and maquina_opcion == 'tijera') or \
             (usuario_opcion == 'papel' and maquina_opcion == 'piedra') or \
             (usuario_opcion == 'tijera' and maquina_opcion == 'papel'):
            print("¡Ganaste!")  # Usuario gana
            victorias_usuario += 1  # Incrementa las victorias del usuario
        else:
            print("¡Perdiste!")  # Usuario pierde
            victorias_maquina += 1  # Incrementa las victorias de la máquina

    # Al final del juego
    if victorias_usuario == 3:
        print("¡Felicidades, ganaste la partida!")  # Mensaje de victoria
        usuarios[usuario]['victorias'] += 1  # Incrementa las victorias del usuario en el diccionario
        guardar_usuarios()  # Guarda los cambios después de jugar
    else:
        print("La máquina ganó la partida.")  # Mensaje de derrota

def mostrar_ranking():
    """Muestra el ranking de usuarios basado en sus victorias."""
    print("\nRanking de usuarios:")  # Encabezado del ranking
    # Ordena los usuarios por victorias en orden descendente
    ranking = sorted(usuarios.items(), key=lambda x: x[1]['victorias'], reverse=True)
    for usuario, datos in ranking:  # Itera sobre el ranking
        # Muestra el nombre del usuario y sus victorias
        print(f"{datos['nombre']}: {datos['victorias']} victorias")

def main():
    """Función principal para manejar el flujo del juego."""
    while True:  # Bucle principal
        print("\n1. Registrar usuario")  # Opción para registrar usuario
        print("2. Iniciar sesión")  # Opción para iniciar sesión
        print("3. Salir")  # Opción para salir
        opcion = input("Elige una opción: ")  # Solicita una opción al usuario

        if opcion == '1':
            registrar_usuario()  # Llama a la función para registrar usuario
        elif opcion == '2':
            usuario = login_usuario()  # Llama a la función para iniciar sesión
            if usuario:  # Si el login fue exitoso
                while True:  # Bucle para jugar
                    jugar(usuario)  # Llama a la función para jugar
                    mostrar_ranking()  # Muestra el ranking después de cada partida
                    jugar_otra = input("¿Quieres jugar otra partida? (s/n): ").lower()  # Pregunta si quiere jugar otra
                    if jugar_otra != 's':  # Si no quiere jugar más
                        break  # Sale del bucle de juego
        elif opcion == '3':
            print("Saliendo del juego. ¡Hasta luego!")  # Mensaje de despedida
            break  # Sale del bucle principal y termina el programa
        else:
            print("Opción inválida. Por favor elige una opción válida.")  # Mensaje de error

# Ejecuta la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()  # Llama a la función main

