from datetime import datetime

class Tarea:
    def __init__(self, descripcion, fecha_vencimiento=None, prioridad=None):
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad

    def __str__(self):
        fecha_vencimiento_str = self.fecha_vencimiento.strftime('%d/%m/%Y') if self.fecha_vencimiento else 'Sin fecha de vencimiento'
        prioridad_str = f'Prioridad: {self.prioridad}' if self.prioridad else 'Sin prioridad'
        return f'Tarea: {self.descripcion} | Fecha de Vencimiento: {fecha_vencimiento_str} | {prioridad_str}'

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def editar_tarea(self, indice, tarea):
        self.tareas[indice] = tarea

    def eliminar_tarea(self, indice):
        del self.tareas[indice]

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f'{i + 1}. {tarea}')

def obtener_fecha():
    fecha_str = input("Ingrese la fecha de vencimiento (DD/MM/AAAA): ")
    try:
        return datetime.strptime(fecha_str, '%d/%m/%Y')
    except ValueError:
        print("Formato de fecha inválido. Por favor, utilice DD/MM/AAAA.")
        return obtener_fecha()

def main():
    lista_tareas = ListaDeTareas()

    while True:
        print("\nMenú de Lista de Tareas:")
        print("1. Agregar Tarea")
        print("2. Editar Tarea")
        print("3. Eliminar Tarea")
        print("4. Mostrar Tareas")
        print("5. Salir")

        opcion = input("Ingrese su elección (1-5): ")

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_vencimiento = obtener_fecha()
            prioridad = input("Ingrese la prioridad de la tarea (opcional): ")
            tarea = Tarea(descripcion, fecha_vencimiento, prioridad)
            lista_tareas.agregar_tarea(tarea)
            print("¡Tarea agregada exitosamente!")

        elif opcion == '2':
            lista_tareas.mostrar_tareas()
            indice = int(input("Ingrese el índice de la tarea que desea editar: ")) - 1
            descripcion = input("Ingrese la descripción actualizada de la tarea: ")
            fecha_vencimiento = obtener_fecha()
            prioridad = input("Ingrese la prioridad actualizada de la tarea (opcional): ")
            tarea = Tarea(descripcion, fecha_vencimiento, prioridad)
            lista_tareas.editar_tarea(indice, tarea)
            print("¡Tarea editada exitosamente!")

        elif opcion == '3':
            lista_tareas.mostrar_tareas()
            indice = int(input("Ingrese el índice de la tarea que desea eliminar: ")) - 1
            lista_tareas.eliminar_tarea(indice)
            print("¡Tarea eliminada exitosamente!")

        elif opcion == '4':
            lista_tareas.mostrar_tareas()

        elif opcion == '5':
            print("Saliendo del programa. ¡Adiós!")
            break

        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")

if __name__ == "__main__":
    main()