def exchange_money(cantidad, tasa_origen, tasa_destino):
    return (cantidad * tasa_origen) / tasa_destino

def mostrar_opciones():
    print("\n--- Convertidor de Monedas ---")
    print("1. Pesos Dominicanos (DOP)")
    print("2. Dólares (USD)")
    print("3. Yenes Japoneses (JPY)")
    print("4. Euros (EUR)")
    print("5. Pesos Mexicanos (MXN)")
    print("6. Pesos Colombianos (COP)")
    print("7. Dólares Canadienses (CAD)")
    print("8. Libras Esterlinas (GBP)")
    print("9. Francos Suizos (CHF)")
    print("10. Pesos Argentinos (ARS)")
    print("11. Reales Brasileños (BRL)")

def obtener_tasa(opcion):
    tasas = {
        1: 1.00,      
        2: 58.00,     
        3: 0.38,      
        4: 64.70,     
        5: 3.26,      
        6: 0.015,     
        7: 42.70,     
        8: 72.60,    
        9: 66.50,     
        10: 0.062,    
        11: 11.80     
    }
    return tasas.get(opcion)

def obtener_nombre(opcion):
    monedas = {
        1: "DOP", 2: "USD", 3: "JPY", 4: "EUR", 5: "MXN", 6: "COP",
        7: "CAD", 8: "GBP", 9: "CHF", 10: "ARS", 11: "BRL"
    }
    return monedas.get(opcion)

def main():
    while True:
        mostrar_opciones()
        try:
            origen = int(input("Elige la moneda de ORIGEN (1-11): "))
            destino = int(input("Elige la moneda DESTINO (1-11): "))
            
            if origen not in range(1, 12) or destino not in range(1, 12):
                print(" Opción no válida.")
                continue
            if origen == destino:
                print(" La moneda de origen y destino no pueden ser iguales.")
                continue

            cantidad = float(input(f"Introduce la cantidad en {obtener_nombre(origen)}: "))
            tasa_origen = obtener_tasa(origen)
            tasa_destino = obtener_tasa(destino)

            resultado = exchange_money(cantidad, tasa_origen, tasa_destino)

            print(f"\n💱 {cantidad} {obtener_nombre(origen)} equivalen a {resultado:.2f} {obtener_nombre(destino)}")

        except ValueError:
            print(" Entrada inválida. Asegúrate de escribir números.")
            continue

        repetir = input("\n¿Deseas hacer otra conversión? (sí / no): ").strip().lower()
        if repetir != "si":
            print("¡Gracias por usar el convertidor! Hasta la próxima.")
            break

if __name__ == "__main__":
    main()
