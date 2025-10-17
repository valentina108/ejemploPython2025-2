nombres = [] #lista vacia

for i in range(3): #las veces que se repite
    nombre = input("ingrese un nombre: ") #se pide el nombre
    nombres.append(nombre) #se agrega el nombre a la lista

mayor = nombres[0] #asignar el primer nombre como el mayor inicialmente
for nombre in nombres: #recorrer la lista de nombres
    if len(nombre) > len(mayor): #comparar la longitud de los nombres
        mayor = nombre #actualizar el mayor si se encuentra uno más largo
    
print("Nombre ingresados: ",nombres) #mostrar la lista de nombres
print("Nombre con más caracteres: ",mayor) #mostrar el nombre con más caracteres