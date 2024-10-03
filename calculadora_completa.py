def suma(*args):
    """Devuelve la suma de los números pasados como parámetros."""
    try:
        # Intenta convertir cada argumento a float y sumarlos
        return sum(float(num) for num in args)
    except ValueError:
        # Si hay un error en la conversión, devuelve un mensaje de error
        return "Error: Todos los parámetros deben ser números."

def resta(a, b):
    """Devuelve la resta de dos números."""
    try:
        # Convierte los parámetros a float y realiza la resta
        return float(a) - float(b)
    except ValueError:
        # Si hay un error en la conversión, devuelve un mensaje de error
        return "Error: Los parámetros deben ser números."

def multiplicar(a, b):
    """Devuelve el resultado de multiplicar dos números."""
    try:
        # Convierte los parámetros a float y realiza la multiplicación
        return float(a) * float(b)
    except ValueError:
        # Si hay un error en la conversión, devuelve un mensaje de error
        return "Error: Los parámetros deben ser números."

def dividir(a, b):
    """Devuelve el resultado de dividir dos números."""
    try:
        # Convierte los parámetros a float
        a, b = float(a), float(b)
        # Maneja la división entre cero
        if b == 0:
            return "Error: No se puede dividir entre cero."
        # Realiza la división y devuelve el resultado
        return a / b
    except ValueError:
        # Si hay un error en la conversión, devuelve un mensaje de error
        return "Error: Los parámetros deben ser números."

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nPrueba de Calculadora con Python:")  # Imprime el título del menú
    print("1. Sumar")  # Opción para sumar
    print("2. Restar")  # Opción para restar
    print("3. Multiplicar")  # Opción para multiplicar
    print("4. Dividir")  # Opción para dividir
    print("5. Ver historial")  # Opción para ver el historial
    print("6. Salir")  # Opción para salir

def guardar_historico(operacion):
    """Guarda la operación en un archivo de texto."""
    # Abre el archivo 'historico.txt' en modo append
    with open("historico.txt", "a") as archivo:
        # Escribe la operación en una nueva línea
        archivo.write(operacion + "\n")

def mostrar_historico():
    """Muestra el historial de operaciones guardadas en el archivo."""
    try:
        # Intenta abrir el archivo 'historico.txt' en modo lectura
        with open("historico.txt", "r") as archivo:
            lineas = archivo.readlines()  # Lee todas las líneas del archivo, se usa para leer todas las líneas de un archivo y devolverlas como una lista de cadenas (strings).
            if lineas:
                print("\nHistorial de operaciones:")  # Imprime el encabezado
                # Imprime cada línea del historial
                for linea in lineas:
                    print(linea.strip())  # Elimina espacios en blanco y muestra la línea
            else:
                print("No hay operaciones en el historial.")  # Mensaje si el historial está vacío
    except FileNotFoundError:
        # Maneja el caso donde el archivo no existe
        print("No se encontró el archivo en el historial.")

def main():
    """Función principal que ejecuta el programa."""
    while True:  # Bucle infinito para mantener el programa en ejecución
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Seleccione una opción: ")  # Solicita la opción al usuario

        if opcion == '1':
            # Suma
            numeros = input("Ingrese los números para la suma separados por comas ('Ej.: 3, 4, 5, ...'): ")
            numeros_lista = numeros.split(",")  # Separa los números en una lista
            resultado = suma(*numeros_lista)  # Llama a la función de suma
            print(f"Resultado de la suma: {resultado}")  # Muestra el resultado
            # Guarda en el historial
            guardar_historico(f"Suma: {' + '.join(numeros_lista)} = {resultado}")

        elif opcion == '2':
            # Resta
            a = input("Ingrese el primer número: ")  # Solicita el primer número
            b = input("Ingrese el segundo número: ")  # Solicita el segundo número
            resultado = resta(a, b)  # Llama a la función de resta
            print(f"Resultado de la resta: {resultado}")  # Muestra el resultado
            guardar_historico(f"Resta: {a} - {b} = {resultado}")

        elif opcion == '3':
            # Multiplicación
            a = input("Ingrese el primer número: ")  # Solicita el primer número
            b = input("Ingrese el segundo número: ")  # Solicita el segundo número
            resultado = multiplicar(a, b)  # Llama a la función de multiplicación
            print(f"Resultado de la multiplicación: {resultado}")  # Muestra el resultado
            guardar_historico(f"Multiplicación: {a} * {b} = {resultado}")

        elif opcion == '4':
            # División
            a = input("Ingrese el primer número: ")  # Solicita el primer número
            b = input("Ingrese el segundo número: ")  # Solicita el segundo número
            resultado = dividir(a, b)  # Llama a la función de división
            print(f"Resultado de la división: {resultado}")  # Muestra el resultado
            guardar_historico(f"División: {a} / {b} = {resultado}")

        elif opcion == '5':
            # Mostrar historial
            mostrar_historico()  # Llama a la función para mostrar el historial

        elif opcion == '6':
            # Salir del programa
            print("Saliendo del programa...")  # Mensaje de salida
            break  # Sale del bucle y termina el programa

        else:
            # Opción no válida
            print("Opción no válida. Por favor, elija nuevamente.")  # Mensaje de error

if __name__ == "__main__":
    main()  # Llama a la función principal para ejecutar el programa