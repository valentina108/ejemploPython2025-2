#promedioNotas
sw = 1
listaNotas = []
print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción: "))

if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            nota=int(input("Incorpore su nota, si desea salir, presione 0: "))
            if(nota != 0):
                listaNotas.append(nota)
                print(f"notas ingresadas: {listaNotas}")
                print(f"cantidad de notas ingresadas: {len(listaNotas)}")
                promedio = sum(listaNotas)/len(listaNotas)
                print(f"El promedio de sus notas es: {promedio}")
            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
        else:
            print("Adiós")


#Completar con las sentencias de código, que permitan realizar:
#1.- Agregar notas a la lista creada
#2.- Muestre por pantalla todas las notas ingresadas
#3.- Muestra la cantidad de notas ingresadas
#4.- Obtenga el promedio de las notas