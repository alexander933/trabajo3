class Cine:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.asientos_disponibles = [[True for _ in range(columnas)] for _ in range(filas)]

    def mostrar_disponibilidad(self):
        print("Disponibilidad de asientos:")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.asientos_disponibles[i][j]:
                    print("O", end=" ")
                else:
                    print("X", end=" ")
            print()

    def reservar_asiento(self, fila, columna):
        if fila < 1 or fila > self.filas or columna < 1 or columna > self.columnas:
            print("Fila o columna inválida.")
            return False
        elif not self.asientos_disponibles[fila - 1][columna - 1]:
            print("El asiento ya está reservado.")
            return False
        else:
            self.asientos_disponibles[fila - 1][columna - 1] = False
            print("¡Reserva exitosa!")
            return True


def main():
    print("¡Bienvenido al sistema de reservas de cine!")

    filas = int(input("Ingrese el número de filas del cine: "))
    columnas = int(input("Ingrese el número de columnas del cine: "))

    cine = Cine(filas, columnas)

    while True:
        print("\nMenú:")
        print("1. Mostrar disponibilidad de asientos")
        print("2. Reservar un asiento")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cine.mostrar_disponibilidad()
        elif opcion == "2":
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))
            cine.reservar_asiento(fila, columna)
        elif opcion == "3":
            print("¡Gracias por usar nuestro sistema de reservas de cine!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()