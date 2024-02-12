import random

def generar_historia():
    personajes = ["Juan", "María", "Pedro", "Ana", "Luisa", "Carlos"]
    lugares = ["ciudad", "pueblo", "montaña", "playa", "bosque"]
    eventos = ["encontraron un tesoro", "se perdieron", "rescataron a un animal", "descubrieron un misterio"]

    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    evento = random.choice(eventos)

    historia = f"{personaje} estaba en un {lugar} cuando {evento}."
    return historia

def main():
    print("¡Bienvenido al generador de historias aleatorias!")

    while True:
        print("\nMenú:")
        print("1. Generar historia")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            historia = generar_historia()
            print("Historia generada:")
            print(historia)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()