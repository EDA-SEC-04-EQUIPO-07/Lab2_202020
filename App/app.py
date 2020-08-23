"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 

from Sorting import insertionsort as ins
from Sorting import selectionsort as sel
from Sorting import shellsort as she

def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList("ARRAY_LIST") #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",(t1_stop-t1_start)," segundos")
    return lst


def less(element1, element2, criteria):
    if float(element1[criteria]) < float(element2[criteria]):
        return True
    return False

def greater (element1,element2, criteria):
    if float(element1[criteria]) > float(element2[criteria]):
        return True
    return False


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Ordenar elementos")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, lst1,lst2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    lst = lt.newList()
    promedio=0
    ids=[]

    iterator = it.newIterator(lst1)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        if criteria.lower() in element["director_name"].lower(): 
            lt.addLast(lst,element)
            ids.append(element["id"])
    
    iterator = it.newIterator(lst2)
    while  it.hasNext(iterator):
        pelicula = it.next(iterator)
        if pelicula["id"] in ids: 
            promedio+=float(pelicula["vote_average"])
    promedio/=lst["size"]
    
    return (lst,lst["size"],promedio)

def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if column == "1":
        column="vote_count"
    elif column == "2":
        column="vote_average"
    else:
        print("Valor no valido para criterio de busqueda")
    lista=[]
    if function.lower()=="crecimiento":
        ins.insertionSort(lst,greater,column)
    elif function.lower()=="decrecimiento":
        ins.insertionSort(lst,less,column)
    for i in range(0,int(elements)):
        lista.append(lt.getElement(lst, i)["original_title"])
    return lista

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados
    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_casting = lt.newList()   # se require usar lista definida
    lista_details = lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista_casting = loadCSVFile("Data/MoviesCastingRaw-small.csv") #llamar funcion cargar datos
                lista_details = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv")
                print("Datos cargados en lista casting, ",lista_casting['size']," elementos cargados")
                print("Datos cargados en lista details, ",lista_details['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")    
                else: print("La lista details tiene ",lista_details['size']," elementos y la lista casting tiene ",lista_casting['size']," elementos" )
            elif int(inputs[0])==3: #opcion 3
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")  
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "director_name", lista_casting) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")
                else:
                    criteria =input('Ingrese el nombre del director\n')
                    print(countElementsByCriteria(criteria,lista_casting,lista_details))
                    lista,counter,promedio=countElementsByCriteria(criteria,lista_casting,lista_details)
                    print("Las peliculas dirigidas por " + criteria +  " son "+ str(lista))
                    print ("Hay "+str(counter)+" películas buenas de ese director. Y "+str(promedio)+" es su promedio de la votacion.") 
            elif int(inputs[0])==5: #opcion 5
                if lista_details==None or lista_details['size']==0: #obtener la longitud de la lista
                    print("La lista details esta vacía")  
                elif lista_casting==None or lista_casting['size']==0: #obtener la longitud de la lista
                    print("La lista casting esta vacía")
                else:
                    criteria =input('Ingrese 1 si el criterio de busqueda es COUNT o ingrese 2 si es AVERAGE\n')
                    crecimiento =input("¿Quiere la lista en crecimiento o decrecimiento?\n")
                    tamaño =input("Ingrese cuantas posiciones quiere que tenga su lista\n")
                    lista=orderElementsByCriteria(crecimiento,criteria,lista_details,tamaño)
                    print ("La lista de peliculas solicitada es:",lista)
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()
