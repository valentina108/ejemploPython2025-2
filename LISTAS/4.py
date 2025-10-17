usuarios = []
contrasenas = []

while True:
    try:
        print("----MENU----")
        print("1. Inicio sesión.")
        print("2. Registrar usuario")
        print("3. Eliminar usuario.")
        print("4. Salir.")

        opc = int(input("Seleccione una opción (1-4): "))

        if opc == 1:
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")

            i = 0
            encontrado = False
            while i < len(usuarios):
                if usuarios[i] == usuario and contrasenas[i] == contrasena:
                    encontrado = True
                    break
                i = i + 1

            if encontrado:
                print("Inicio de sesion exitoso.")
            else:
                print("Usuario o contraseña incorrectos.")
        elif opc == 2:
            usuario = input("Ingrese nuevo usuario: ")
            existe = False
            i = 0
            while i < len(usuarios):
                if usuarios[i] == usuario:
                    existe = True
                    break
                i = i + 1
            if existe:
                print("Usuario ya existe.")
                continue
            usuarios.append(usuario)
            contrasena = input("Contraseña: ")
            contrasenas.append(contrasena)
            print("Usuario registrado exitosamente.")
        
        elif opc == 3:
            usuario = input("Usuario a eliminar: ")
            contrasena = input("confirme contraseña para eliminar:  ")

            i = 0
            eliminado = False
            while i < len(usuarios):
                if usuarios[i] == usuario and contrasenas[i] == contrasena:

                    usuarios.pop(i)
                    contrasenas.pop(i)
                    eliminado = True
                    break
                i = i + 1
                if eliminado:
                    print("Usuario eliminado exitosamente.")
                else:
                    print("No se pudo eliminar el usuario. Verifique las credenciales.")

        elif opc == 4:
            print("gracias...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entre 1 y 4.")