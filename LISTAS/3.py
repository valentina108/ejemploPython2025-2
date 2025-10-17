nombres = [] #lista vacia

while True: #bucle infinito para agregar nombres
    nombre = input("Ingrese un nombre: ") #se pide el nombre
    nombres.append(nombre) #se agrega el nombre a la lista

    seguir = input("¿Desea agregar otro nombre? (si/no): ").lower() #preguntar si quiere seguir
    if seguir == "no": #si no quiere seguir
        break #romper el bucle

menor = nombres[0] #asignar el primer nombre como el mas corto inicialmente
for nom in nombres: #recorrer la lista de nombres
    if len(nom) < len(menor): #comparar longitudes
        menor = nom #actualizar el nombre mas corto

nombres.remove(menor) #eliminar el nombre mas corto de la lista
print(f"Se elimino '{menor}' ya que es el nombre mas corto.") #mostrar mensaje
print("Lista final: ", nombres) #mostrar la lista final