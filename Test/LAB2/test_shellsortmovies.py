import pytest
import config as cf
from Sorting import shellsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

list_type = 'ARRAY_LIST'
#list_type = 'SINGLE_LINKED'

lst_movies = lt.newList(list_type)
moviesfile = cf.data_dir + 'SmallMoviesDetailsCleaned.csv'

def setUp():
    print('Loading movies')
    loadCSVFile(moviesfile, lst_movies)
    print(lst_movies['size'])


def tearDown():
       pass


def loadCSVFile(file, lst):
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['id'])

def less(element1, element2):
    if int(element1['id']) < int(element2['id']):
        return True
    return False

def test_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.shellSort(lst_movies, less)

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.shellSort(lst_movies,less)
  while not (lt.isEmpty(lst_movies)):
        x = int(lt.removeLast(lst_movies)['id'])
        if not (lt.isEmpty(lst_movies)):
            y = int(lt.lastElement(lst_movies)['id'])
        else:
            break
        assert x > y
