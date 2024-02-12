class RegistroGastos:
    def __init__(self):
        self.gastos = {}

    def agregar_gasto(self, categoria, monto):
        if categoria in self.gastos:
            self.gastos[categoria] += monto
        else:
            self.gastos[categoria] = monto

    def total_por_categoria(self):
        return self.gastos

    def total_general(self):
        return sum(self.gastos.values())

def main():
    registro = RegistroGastos()

    while True:
        print("\nMenú:")
        print("1. Agregar gasto")
        print("2. Ver total por categoría")
        print("3. Ver total general de gastos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            categoria = input("Ingrese la categoría del gasto: ")
            monto = float(input("Ingrese el monto del gasto: "))
            registro.agregar_gasto(categoria, monto)
            print("Gasto agregado correctamente.")
        elif opcion == "2":
            total_por_categoria = registro.total_por_categoria()
            print("\nTotal por categoría:")
            for categoria, total in total_por_categoria.items():
                print(f"{categoria}: ${total}")
        elif opcion == "3":
            total_general = registro.total_general()
            print(f"\nTotal general de gastos: ${total_general}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()