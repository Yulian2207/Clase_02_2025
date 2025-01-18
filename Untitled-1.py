#1. ¿Que es un arreglo?
#Es una lista para una estructura de datos que almacena una secuencia de elementos de forma consecutiva.
#Y cada elemento se puede encontrar por medio de su indice (el indice comienza dese 0)

#2. Uso común del concepto de los vectores / arreglo / array / listas:
#Guarda datos relacionados como números, nombres o resultados.
#Procesar grandes cantitades de nformación esto de forma ordenada.

#3. ¿Cuales so sus operaciones basicas?
#se crean y se llenan.
#Recorrer y manipular datos.
#Realizar busquedas, filtros y transformaciones.



#Ejemplos detallados:
#Llenar y mostrar un vector.

vector = []

#Vamos a llenar el vector por valores definidos por un usuario.
for i in range (5):
    valor = int(input(f"Ingrese un número para la posición {i}: "))
    vector.append (valor) #.append es una función interna de python que recibe como parametro
                #lo que se va a agregar a un arreglo y lo coloca en la ultima posición disponible.
                                         
print (f"Arreglo ingresado: {vector}")

#Revorrer y modificar valores dentro de un vector / arreglo / array.

vector2 = [10, 20, 30, 40, 50]
#Lo recorremos o lo iteramos, haciendo alguna operación en cada uno de los elementos que contiene el arreglo.
#Lamenjor manera de hacverlo es con un ciclo for.
print ("Elementos originales")
for i in range (len(vector2)):#len cuenta cuantos elementos tiene el vextor y se utiliza para ahacer algunas.
#operaciones básicas.
       print (f"Indice {i}: {vector[i]}")#[]Hace referencia a la posición donde esta cada elemento del arreglo.

#Modificar cada elemento multiplicado por dos.
for i in range (len(vector2)):
    vector2[i] *= 2#Se modifica un elemento llamando a su posición en el indice 
    #e igualdad al nuevo valor que se le quiere asignar

#Volvemos a imprimirlo: 
print ("Vector luego de ser modificado")
for i in range (len(vector2)):
    print (f"Indice {i}: {vector2[i]}")
