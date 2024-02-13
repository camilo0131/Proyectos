def longitud():
    print("\nConversión de Longitud")
    print("1. Metros a Centímetros")
    print("2. Centímetros a Metros")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    opcion = input("Ingrese su elección (1-4): ")

    if opcion == '1':
        metros = float(input("Ingrese la longitud en metros: "))
        centimetros = metros * 100
        print(f"{metros} metros son {centimetros} centímetros.")
    elif opcion == '2':
        centimetros = float(input("Ingrese la longitud en centímetros: "))
        metros = centimetros / 100
        print(f"{centimetros} centímetros son {metros} metros.")
    elif opcion == '3':
        kilometros = float(input("Ingrese la longitud en kilómetros: "))
        millas = kilometros / 1.60934
        print(f"{kilometros} kilómetros son {millas} millas.")
    elif opcion == '4':
        millas = float(input("Ingrese la longitud en millas: "))
        kilometros = millas * 1.60934
        print(f"{millas} millas son {kilometros} kilómetros.")
    else:
        print("Opción no válida.")

def masa():
    print("\nConversión de Masa")
    print("1. Kilogramos a Gramos")
    print("2. Gramos a Kilogramos")
    print("3. Libras a Kilogramos")
    print("4. Kilogramos a Libras")
    opcion = input("Ingrese su elección (1-4): ")

    if opcion == '1':
        kg = float(input("Ingrese la masa en kilogramos: "))
        gramos = kg * 1000
        print(f"{kg} kilogramos son {gramos} gramos.")
    elif opcion == '2':
        gramos = float(input("Ingrese la masa en gramos: "))
        kg = gramos / 1000
        print(f"{gramos} gramos son {kg} kilogramos.")
    elif opcion == '3':
        libras = float(input("Ingrese la masa en libras: "))
        kg = libras * 0.453592
        print(f"{libras} libras son {kg} kilogramos.")
    elif opcion == '4':
        kg = float(input("Ingrese la masa en kilogramos: "))
        libras = kg / 0.453592
        print(f"{kg} kilogramos son {libras} libras.")
    else:
        print("Opción no válida.")

def temperatura():
    print("\nConversión de Temperatura")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Ingrese su elección (1-2): ")

    if opcion == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
    elif opcion == '2':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
    else:
        print("Opción no válida.")

def main():
    while True:
        print("\nMenú de Conversión")
        print("1. Longitud")
        print("2. Masa")
        print("3. Temperatura")
        print("4. Salir")
        opcion = input("Ingrese su elección (1-4): ")

        if opcion == '1':
            longitud()
        elif opcion == '2':
            masa()
        elif opcion == '3':
            temperatura()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()