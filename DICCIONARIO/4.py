# ...existing code...

#1
def crear_diccionario_usuario(nombre, sexo, contrasena):
    usuario = {'nombre': nombre, 'sexo': sexo, 'contrasena': contrasena}
    return usuario
usuario_ej = crear_diccionario_usuario('L.Pereira', 'F', 'as1234yuioj')
print(f"Diccionario Usuario: {usuario_ej}")

#2
def validar_sexo(sexo):
    sexo = sexo.upper()
    return sexo == "M" or sexo == "F"
print(f"Validar 'M': {validar_sexo('M')}")
print(f"Validar 'o': {validar_sexo('o')}")

#3
def validar_contrasena(clave):
    if len(clave) < 8:  # Condición 1: Mínimo 8 caracteres
        return "Error: La clave es muy corta."
    if not any(c.isdigit() for c in clave):  # Condición 2: Debe tener un número
        return "Error: La clave debe incluir un número."
    return "Contraseña válida"

print(f"Validar 'abc12345': {validar_contrasena('abc12345')}")

#4
USUARIOS = []
def agregar_usuario_validado(lista, nombre, sexo, contrasena):
    nombres_existentes = [u['nombre'] for u in lista]
    if nombre in nombres_existentes:
        return "Error: Nombre de usuario ya existe."
    if not validar_sexo(sexo):
        return "Error: Sexo inválido (M o F)."
    resultado_clave = validar_contrasena(contrasena)
    if resultado_clave.startswith("Error"):
        return resultado_clave
    nuevo_usuario = crear_diccionario_usuario(nombre, sexo, contrasena)
    lista.append(nuevo_usuario)
    return "Usuario ingresado con éxito"

print(agregar_usuario_validado(USUARIOS, 'Juan', 'M', 'abc12345'))
print(agregar_usuario_validado(USUARIOS, 'Ana', 'F', 'qwertyui'))

#5
def mostrar_usuarios(lista_usuarios):
    print("\n--- Listado de Usuarios ---")
    for usuario in lista_usuarios:
        nombre = usuario['nombre']
        sexo = usuario['sexo']
        print(f"Usuario: {nombre}, Sexo: {sexo}")

mostrar_usuarios(USUARIOS)
# ...existing code...