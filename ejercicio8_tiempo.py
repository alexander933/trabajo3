import random

class SimuladorTiempo:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def temperatura_actual(self):
        return round(random.uniform(10, 30), 2)  # Temperatura en grados Celsius

    def estado_cielo_actual(self):
        estados_cielo = ["Despejado", "Nublado", "Parcialmente nublado", "Lluvia ligera", "Lluvia intensa", "Tormenta"]
        return random.choice(estados_cielo)

    def velocidad_viento_actual(self):
        return round(random.uniform(0, 30), 2)  # Velocidad del viento en km/h

    def informacion_actual(self):
        temperatura = self.temperatura_actual()
        estado_cielo = self.estado_cielo_actual()
        velocidad_viento = self.velocidad_viento_actual()

        return f"Ubicación: {self.ubicacion}\nTemperatura: {temperatura}°C\nEstado del cielo: {estado_cielo}\nVelocidad del viento: {velocidad_viento} km/h"


def main():
    ubicacion = input("Ingrese la ubicación para obtener información meteorológica simulada: ")
    simulador = SimuladorTiempo(ubicacion)

    informacion = simulador.informacion_actual()
    print("\nInformación meteorológica simulada:")
    print(informacion)


if __name__ == "__main__":
    main()