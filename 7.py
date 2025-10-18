"""
def agregar_usuario(lista, nombre):
    if nombre not in lista:      # Verifica si el nombre no está en la lista
        lista.append(nombre)     # Si no está, lo agrega
    else:
        print("El usuario ya existe.")
    
    print(lista)                 # Muestra la lista actualizada


# --- Programa principal ---
usuarios = ['Ana']               # Lista inicial
agregar_usuario(usuarios, 'Pedro')
"""

def agregar_usuario(lista, nombre):
    if nombre not in lista:
        lista.append(nombre)
    print(lista)

# Ejemplo
usuarios = ['Ana']
agregar_usuario(usuarios, 'Pedro')