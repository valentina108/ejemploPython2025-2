nombres = [] #lista vacia
apellidos = [] #lista vacia

for i in range(3): #las veces que se repite
    nombre = input(f"Ingrese nombre N° {i+1}: ") #se pide el nombre
    nombres.append(nombre) #se agrega el nombre a la lista

for i in range(3): #las veces que se repite
    apellido = input(f"Ingrese apellido N° {i+1}: ") #se pide el apellido
    apellidos.append(apellido) #se agrega el apellido a la lista

print("Listado ordenado de nombres y apellidos: ") #mostrar el listado

for i in range(3): #recorrer las listas
    if i < 3: #condicion para evitar error de indice
        print(f"{nombres[i]} {apellidos[i]}") #mostrar nombre y apellido juntos 