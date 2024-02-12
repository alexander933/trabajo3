class BancoDeDatos:
    def __init__(self):
        self.registros = {}

    def agregar_registro(self, clave, valor):
        self.registros[clave] = valor
        print("Registro agregado correctamente.")

    def actualizar_registro(self, clave, valor):
        if clave in self.registros:
            self.registros[clave] = valor
            print("Registro actualizado correctamente.")
        else:
            print("La clave no existe en la base de datos.")

    def eliminar_registro(self, clave):
        if clave in self.registros:
            del self.registros[clave]
            print("Registro eliminado correctamente.")
        else:
            print("La clave no existe en la base de datos.")

    def buscar_registro(self, clave):
        if clave in self.registros:
            print(f"Registro encontrado: {self.registros[clave]}")
        else:
            print("La clave no existe en la base de datos.")

    def visualizar_registros(self):
        print("Registros en la base de datos:")
        for clave, valor in self.registros.items():
            print(f"Clave: {clave}, Valor: {valor}")


def main():
    banco_de_datos = BancoDeDatos()

    while True:
        print("\nMenu:")
        print("1. Agregar registro")
        print("2. Actualizar registro")
        print("3. Eliminar registro")
        print("4. Buscar registro")
        print("5. Visualizar registros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clave = input("Ingrese la clave del nuevo registro: ")
            valor = input("Ingrese el valor del nuevo registro: ")
            banco_de_datos.agregar_registro(clave, valor)
        elif opcion == "2":
            clave = input("Ingrese la clave del registro a actualizar: ")
            valor = input("Ingrese el nuevo valor del registro: ")
            banco_de_datos.actualizar_registro(clave, valor)
        elif opcion == "3":
            clave = input("Ingrese la clave del registro a eliminar: ")
            banco_de_datos.eliminar_registro(clave)
        elif opcion == "4":
            clave = input("Ingrese la clave del registro a buscar: ")
            banco_de_datos.buscar_registro(clave)
        elif opcion == "5":
            banco_de_datos.visualizar_registros()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()