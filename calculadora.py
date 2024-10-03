import math  # Importa el módulo math para usar funciones matemáticas

def suma(a, b):
    """Devuelve la suma de a y b. Maneja errores de tipo."""
    try:
        return a + b  # Intenta sumar a y b
    except TypeError:
        return "Error: Ambos parámetros deben ser números."  # Captura el error si no son números

def resta(a, b):
    """Devuelve la resta de a y b. Maneja errores de tipo."""
    try:
        return a - b  # Intenta restar b de a
    except TypeError:
        return "Error: Ambos parámetros deben ser números."  # Captura el error si no son números

def multiplicar(a, b):
    """Devuelve la multiplicación de a y b. Maneja errores de tipo."""
    try:
        return a * b  # Intenta multiplicar a y b
    except TypeError:
        return "Error: Ambos parámetros deben ser números."  # Captura el error si no son números

def dividir(a, b):
    """Devuelve la división de a entre b. Maneja errores de tipo y división por cero."""
    try:
        return a / b  # Intenta dividir a entre b
    except TypeError:
        return "Error: Ambos parámetros deben ser números."  # Captura el error si no son números
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."  # Captura el error de división por cero

def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de a. Maneja errores de tipo y números negativos."""
    try:
        if a < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."  # Verifica si el número es negativo
        return math.sqrt(a)  # Usa math.sqrt para calcular la raíz cuadrada
    except TypeError:
        return "Error: El parámetro debe ser un número."  # Captura el error si no es un número

def mostrar_menu():
    """Muestra un menú de opciones para la calculadora."""
    print("\nCalculadora")
    print("1. Suma")  # Opción para suma
    print("2. Resta")  # Opción para resta
    print("3. Multiplicación")  # Opción para multiplicación
    print("4. División")  # Opción para división
    print("5. Raíz Cuadrada")  # Opción para calcular raíz cuadrada
    print("6. Salir")  # Opción para salir del programa

def main():
    """Función principal que controla el flujo del programa."""
    while True:  # Bucle para mantener el programa en ejecución
        mostrar_menu()  # Muestra el menú
        opcion = input("Elige una opción (1-6): ")  # Solicita la opción al usuario

        if opcion == '1':
            a = float(input("Ingresa el primer número: "))  # Solicita el primer número
            b = float(input("Ingresa el segundo número: "))  # Solicita el segundo número
            print(f"La suma es: {suma(a, b)}")  # Llama a la función suma y muestra el resultado

        elif opcion == '2':
            a = float(input("Ingresa el primer número: "))  # Solicita el primer número
            b = float(input("Ingresa el segundo número: "))  # Solicita el segundo número
            print(f"La resta es: {resta(a, b)}")  # Llama a la función resta y muestra el resultado

        elif opcion == '3':
            a = float(input("Ingresa el primer número: "))  # Solicita el primer número
            b = float(input("Ingresa el segundo número: "))  # Solicita el segundo número
            print(f"La multiplicación es: {multiplicar(a, b)}")  # Llama a la función multiplicar y muestra el resultado

        elif opcion == '4':
            a = float(input("Ingresa el primer número: "))  # Solicita el primer número
            b = float(input("Ingresa el segundo número: "))  # Solicita el segundo número
            print(f"La división es: {dividir(a, b)}")  # Llama a la función dividir y muestra el resultado

        elif opcion == '5':
            a = float(input("Ingresa un número para calcular su raíz cuadrada: "))  # Solicita el número
            print(f"La raíz cuadrada es: {raiz_cuadrada(a)}")  # Llama a la función raíz cuadrada y muestra el resultado

        elif opcion == '6':
            print("Saliendo de la calculadora. ¡Hasta luego!")  # Mensaje de despedida
            break  # Sale del bucle y termina el programa

        else:
            print("Opción inválida. Por favor elige una opción válida.")  # Mensaje de error para opción no válida

# Ejecuta la función principal si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()  # Llama a la función main
