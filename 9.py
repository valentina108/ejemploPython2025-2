def buscar_usuario(lista, nombre):
    return nombre in lista

usuario = ['ana','pedro']
print(buscar_usuario(usuario,'pedro'))
print(buscar_usuario(usuario, 'Juan'))