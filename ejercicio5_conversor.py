def convertir_moneda(cantidad, tasa_cambio):
    return cantidad * tasa_cambio

def main():
    print("¡Bienvenido al conversor de monedas!")
    moneda_origen = input("Ingrese la moneda de origen: ")
    moneda_destino = input("Ingrese la moneda de destino: ")
    cantidad = float(input(f"Ingrese la cantidad de {moneda_origen}: "))

    if moneda_origen == moneda_destino:
        print("Las monedas son iguales. No es necesaria la conversión.")
        return

    if moneda_origen == "USD":
        tasa_cambio = float(input(f"Ingrese la tasa de cambio de 1 {moneda_origen} a {moneda_destino}: "))
    elif moneda_destino == "USD":
        tasa_cambio = float(input(f"Ingrese la tasa de cambio de 1 {moneda_destino} a {moneda_origen}: "))
        tasa_cambio = 1 / tasa_cambio
    else:
        tasa_origen = float(input(f"Ingrese la tasa de cambio de 1 {moneda_origen} a USD: "))
        tasa_destino = float(input(f"Ingrese la tasa de cambio de 1 USD a {moneda_destino}: "))
        tasa_cambio = tasa_destino / tasa_origen

    cantidad_convertida = convertir_moneda(cantidad, tasa_cambio)
    print(f"{cantidad} {moneda_origen} equivale a {cantidad_convertida} {moneda_destino}")

if __name__ == "__main__":
    main()