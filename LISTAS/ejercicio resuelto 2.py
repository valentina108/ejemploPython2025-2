#listaSuper
sw = 1
listaSuper = []
valorSuper = []
print("Presione 1 para ingresar los productos del súper")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción "))
if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            producto=input("Incorpore su producto, para salir, presione 0: ")
            if(producto != "0"):
                listaSuper.append(producto)
                valor_producto = int(input("Incorpore el valor del {producto}: "))
                valorSuper.append(valor_producto)
                print("---DETALLE BOLETA-----")
                print(f"Productos comprados: {listaSuper}")
                print(f"Cantidad de productos comprados: {len(listaSuper)}")
                print(f"Suma total de todos los productos: {sum(valorSuper)}")
            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
        else:
            print("Adiós")

#Completar con las sentencias de código, que permitan realizar:
#1.- Agregar productos a la lista del súper
#2.- Muestre mensaje indicado “Incorpore el valor del {producto}:”
#3.- Agregue el valor del producto a la lista “valorSuper”
#4.- Muestre mensaje indicando “----DETALLE BOLETA-----”
#5.- Muestre mensaje indicando los productos comprados
#6.- Muestre mensaje indicando la cantidad de productos comprados
#7.- Muestre mensaje indicando la suma total de todos los productos#