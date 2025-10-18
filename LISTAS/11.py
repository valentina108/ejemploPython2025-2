#1
def crear_lista_usuarios():
    return []
usuarios = crear_lista_usuarios()
print(f"Lista creada: {usuarios}")

#2
def agregar_usuario_simple(lista, nombre):
    if nombre not in lista:
        lista.append(nombre) 
        return lista
lista_nombres = ['Ana']
lista_nombres = agregar_usuario_simple(lista_nombres, 'Pedro')
print(f"Lista con Pedro: {lista_nombres}")

#3
def contar_usuarios(lista):
    return len(lista)
print(f"Total de usuarios: {contar_usuarios(lista_nombres)}")

# 4
def buscar_usuario_simple(lista, nombre):
    return nombre in lista
print(f"¿Existe 'Pedro'? {buscar_usuario_simple(lista_nombres, 'Pedro')}")

#5
def eliminar_usuario_simple(lista, nombre):
    if nombre in lista:
        lista.remove(nombre) 
        return "Usuario eliminado"
    else:
        return "Usuario no encontrado"
print(eliminar_usuario_simple(lista_nombres, 'Pedro'))
print(f"Lista después de eliminar: {lista_nombres}")