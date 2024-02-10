def longitud():
    print("Seleccione la unidad de longitud:")
    print("1. Metros")
    print("2. Pies")
    opcion = int(input("Ingrese su opción: "))
    valor = float(input("Ingrese el valor: "))
    
    if opcion == 1:
        pies = valor * 3.281
        print(f"{valor} metros son {pies} pies")
    elif opcion == 2:
        metros = valor / 3.281
        print(f"{valor} pies son {metros} metros")
    else:
        print("Opción no válida")

def masa():
    print("Seleccione la unidad de masa:")
    print("1. Kilogramos")
    print("2. Libras")
    opcion = int(input("Ingrese su opción: "))
    valor = float(input("Ingrese el valor: "))
    
    if opcion == 1:
        libras = valor * 2.205
        print(f"{valor} kilogramos son {libras} libras")
    elif opcion == 2:
        kilogramos = valor / 2.205
        print(f"{valor} libras son {kilogramos} kilogramos")
    else:
        print("Opción no válida")

def temperatura():
    print("Seleccione la unidad de temperatura:")
    print("1. Celsius")
    print("2. Fahrenheit")
    opcion = int(input("Ingrese su opción: "))
    valor = float(input("Ingrese el valor: "))
    
    if opcion == 1:
        fahrenheit = (valor * 9/5) + 32
        print(f"{valor} grados Celsius son {fahrenheit} grados Fahrenheit")
    elif opcion == 2:
        celsius = (valor - 32) * 5/9
        print(f"{valor} grados Fahrenheit son {celsius} grados Celsius")
    else:
        print("Opción no válida")

# Función principal
def main():
    print("Bienvenido al Conversor de Unidades")
    print("Seleccione el tipo de conversión:")
    print("1. Longitud")
    print("2. Masa")
    print("3. Temperatura")
    opcion = int(input("Ingrese su opción: "))
    
    if opcion == 1:
        longitud()
    elif opcion == 2:
        masa()
    elif opcion == 3:
        temperatura()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()