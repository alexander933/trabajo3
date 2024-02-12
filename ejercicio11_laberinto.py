import random

class Laberinto:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.laberinto = self.generar_laberinto()

    def generar_laberinto(self):
        laberinto = [["#" for _ in range(self.columnas)] for _ in range(self.filas)]

        for i in range(1, self.filas, 2):
            for j in range(1, self.columnas, 2):
                laberinto[i][j] = " "

        for i in range(1, self.filas, 2):
            for j in range(1, self.columnas, 2):
                if i > 1:
                    laberinto[i - 1][j] = " "
                if i < self.filas - 2:
                    laberinto[i + 1][j] = " "
                if j > 1:
                    laberinto[i][j - 1] = " "
                if j < self.columnas - 2:
                    laberinto[i][j + 1] = " "

        return laberinto

    def mostrar_laberinto(self):
        for fila in self.laberinto:
            print(" ".join(fila))

    def encontrar_camino(self, fila, columna):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
            return False
        elif self.laberinto[fila][columna] == " ":
            self.laberinto[fila][columna] = "X"
            if fila == self.filas - 2 and columna == self.columnas - 2:
                return True
            if (self.encontrar_camino(fila - 1, columna) or self.encontrar_camino(fila + 1, columna) or
                self.encontrar_camino(fila, columna - 1) or self.encontrar_camino(fila, columna + 1)):
                return True
            self.laberinto[fila][columna] = " "
        return False

def main():
    filas = int(input("Ingrese el número de filas del laberinto (debe ser impar y mayor que 3): "))
    columnas = int(input("Ingrese el número de columnas del laberinto (debe ser impar y mayor que 3): "))

    if filas % 2 == 0 or columnas % 2 == 0 or filas < 3 or columnas < 3:
        print("El tamaño del laberinto debe ser impar y mayor que 3.")
        return

    laberinto = Laberinto(filas, columnas)
    print("\nLaberinto generado:")
    laberinto.mostrar_laberinto()

    if laberinto.encontrar_camino(1, 1):
        print("\nSe encontró un camino para salir del laberinto:")
        laberinto.mostrar_laberinto()
    else:
        print("\nNo se encontró ningún camino para salir del laberinto.")

if __name__ == "__main__":
    main()