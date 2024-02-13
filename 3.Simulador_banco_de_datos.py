class BancoDeDatos:
    def __init__(self):
        self.registros = {}

    def agregar_registro(self, clave, valor):
        self.registros[clave] = valor
        print("Registro agregado exitosamente.")

    def actualizar_registro(self, clave, valor):
        if clave in self.registros:
            self.registros[clave] = valor
            print("Registro actualizado exitosamente.")
        else:
            print("La clave no existe en la base de datos.")

    def eliminar_registro(self, clave):
        if clave in self.registros:
            del self.registros[clave]
            print("Registro eliminado exitosamente.")
        else:
            print("La clave no existe en la base de datos.")

    def buscar_registro(self, clave):
        if clave in self.registros:
            print(f"Clave: {clave}, Valor: {self.registros[clave]}")
        else:
            print("La clave no existe en la base de datos.")

    def mostrar_registros(self):
        if self.registros:
            print("Registros en la base de datos:")
            for clave, valor in self.registros.items():
                print(f"Clave: {clave}, Valor: {valor}")
        else:
            print("La base de datos está vacía.")

def main():
    banco_datos = BancoDeDatos()

    while True:
        print("\nMenú del Banco de Datos:")
        print("1. Agregar Registro")
        print("2. Actualizar Registro")
        print("3. Eliminar Registro")
        print("4. Buscar Registro")
        print("5. Mostrar Registros")
        print("6. Salir")

        opcion = input("Ingrese su elección (1-6): ")

        if opcion == '1':
            clave = input("Ingrese la clave del registro: ")
            valor = input("Ingrese el valor del registro: ")
            banco_datos.agregar_registro(clave, valor)
        elif opcion == '2':
            clave = input("Ingrese la clave del registro a actualizar: ")
            valor = input("Ingrese el nuevo valor del registro: ")
            banco_datos.actualizar_registro(clave, valor)
        elif opcion == '3':
            clave = input("Ingrese la clave del registro a eliminar: ")
            banco_datos.eliminar_registro(clave)
        elif opcion == '4':
            clave = input("Ingrese la clave del registro a buscar: ")
            banco_datos.buscar_registro(clave)
        elif opcion == '5':
            banco_datos.mostrar_registros()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
    

    #commit