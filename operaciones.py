"""
Este módulo realiza operaciones básicas: suma, resta, multiplicación y división.
También incluye un menú interactivo para que el usuario elija la operación a realizar.
"""

def suma(valor_uno, valor_dos):
    """Calcula la suma de dos números."""
    return valor_uno + valor_dos


def resta(valor_uno, valor_dos):
    """Calcula la resta de dos números."""
    return valor_uno - valor_dos


def mult(valor_uno, valor_dos):
    """Calcula la multiplicación de dos números."""
    return valor_uno * valor_dos


def div(valor_uno, valor_dos):
    """Calcula la división de dos números. Retorna 'None' si el divisor es 0."""
    if valor_dos == 0:
        print("Error: División por cero.")
        return None
    return valor_uno / valor_dos


def es_par_o_impar(valor):
    """Determina si un número es par o impar."""
    return "PAR" if valor % 2 == 0 else "IMPAR"


def main():
    """
    Muestra un menú interactivo para realizar operaciones básicas.
    Permite al usuario ingresar dos números y elegir la operación.
    """
    while True:
        print("\nSeleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Ingrese su elección (1-5): ")

        if opcion == "5":
            print("¡Gracias por usar el programa!")
            break

        try:
            valor_uno = float(input("Ingrese el primer número: "))
            valor_dos = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Debe ingresar valores numéricos.")
            continue

        if opcion == "1":
            resultado = suma(valor_uno, valor_dos)
            print(f"La suma de {valor_uno} y {valor_dos} es: {resultado}")
        elif opcion == "2":
            resultado = resta(valor_uno, valor_dos)
            print(f"La resta de {valor_uno} y {valor_dos} es: {resultado}")
        elif opcion == "3":
            resultado = mult(valor_uno, valor_dos)
            print(f"La multiplicación de {valor_uno} y {valor_dos} es: {resultado}")
        elif opcion == "4":
            resultado = div(valor_uno, valor_dos)
            if resultado is not None:
                print(f"La división de {valor_uno} entre {valor_dos} es: {resultado}")
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

        # Verificar si el resultado es par o impar (si corresponde)
        if opcion in ["1", "2", "3", "4"] and resultado is not None:
            paridad = es_par_o_impar(resultado)
            print(f"El resultado es un número {paridad}.")


if __name__ == "__main__":
    main()
