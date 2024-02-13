def convertir_moneda(cantidad, tasa):
    return cantidad * tasa

def main():
    print("Bienvenido al Conversor de Monedas")
    print("Por favor, seleccione la moneda de origen:")
    print("1. Dólar estadounidense (USD)")
    print("2. Euro (EUR)")
    print("3. Libra esterlina (GBP)")
    origen = input("Ingrese el número de opción: ")

    if origen not in {'1', '2', '3'}:
        print("Opción no válida.")
        return

    print("\nSeleccione la moneda de destino:")
    print("1. Dólar estadounidense (USD)")
    print("2. Euro (EUR)")
    print("3. Libra esterlina (GBP)")
    destino = input("Ingrese el número de opción: ")

    if destino not in {'1', '2', '3'}:
        print("Opción no válida.")
        return

    cantidad = float(input("\nIngrese la cantidad a convertir: "))

    if origen == '1':
        if destino == '1':
            print("No se requiere conversión. La cantidad es la misma.")
        elif destino == '2':
            tasa = 0.89  # Tasa de cambio de USD a EUR
            resultado = convertir_moneda(cantidad, tasa)
            print(f"{cantidad} USD equivale a {resultado} EUR.")
        elif destino == '3':
            tasa = 0.75  # Tasa de cambio de USD a GBP
            resultado = convertir_moneda(cantidad, tasa)
            print(f"{cantidad} USD equivale a {resultado} GBP.")
    elif origen == '2':
        if destino == '1':
            tasa = 1.12  # Tasa de cambio de EUR a USD
            resultado = convertir_moneda(cantidad, tasa)
            print(f"{cantidad} EUR equivale a {resultado} USD.")
        elif destino == '2':
            print("No se requiere conversión. La cantidad es la misma.")
        elif destino == '3':
            tasa = 0.84  # Tasa de cambio de EUR a GBP
            resultado = convertir_moneda(cantidad, tasa)
            print(f"{cantidad} EUR equivale a {resultado} GBP.")
    elif origen == '3':
        if destino == '1':
            tasa = 1.34  # Tasa de cambio de GBP a USD
            resultado = convertir_moneda(cantidad, tasa)
            print(f"{cantidad} GBP equivale a {resultado} USD.")
        elif destino == '2':
            tasa = 1.19  # Tasa de cambio de GBP a EUR
            resultado = convertir_moneda(cantidad, tasa)
            print(f"{cantidad} GBP equivale a {resultado} EUR.")
        elif destino == '3':
            print("No se requiere conversión. La cantidad es la misma.")

if __name__ == "__main__":
    main()