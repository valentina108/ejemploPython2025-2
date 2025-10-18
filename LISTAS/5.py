canasta = []  # lista para almacenar los productos seleccionados
productos = ["manzana", "pan", "leche", "huevos", "queso"]
precios = [100, 1000, 1100, 30, 200]

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")

    try:
        opc = int(input("Seleccione una opción (1-4): "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    # 1️ Agregar productos
    if opc == 1:
        print("\n--- MENÚ DE PRODUCTOS ---")
        for i in range(len(productos)):
            print(f"{i+1}. {productos[i]} - ${precios[i]}")
        print("6. Volver al menú principal")

        while True:
            try:
                selec = int(input("Seleccione un producto (1-6): "))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            if selec == 6:
                break

            if 1 <= selec <= 5:
                producto = productos[selec - 1]
                precio = precios[selec - 1]
                canasta.append((producto, precio))  # guarda ambos
                print(f"{producto} agregado a la canasta.")
            else:
                print("Opción no válida.")
    
    # 2️ Ver canasta
    elif opc == 2:
        if len(canasta) == 0:
            print("La canasta está vacía.")
        else:
            print("\n--- PRODUCTOS EN LA CANASTA ---")
            for producto, precio in canasta:
                print(f"- {producto} - ${precio}")
    
    # 3️ Ver total
    elif opc == 3:
        if len(canasta) == 0:
            print("La canasta está vacía.")
        else:
            total = sum(precio for _, precio in canasta)
            print(f"\nTotal a pagar: ${total}")
    
    # 4️ Salir
    elif opc == 4:
        print("\nGracias por su compra.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")