def eliminar_usuario(lista, nombre):
    if nombre in lista:
        lista.remove(nombre)
        return "Usuario eliminado"
    else:
        return "Usuario no encontrado"

# Ejemplo
usuarios = ['Ana', 'Pedro']
print(eliminar_usuario(usuarios, 'Pedro'))  # ➜ Usuario eliminado
print(usuarios)