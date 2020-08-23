
import pytest 
import config 
from DataStructures import arraylist as slt



def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def movies ():
    movies = []
    movies.append({'id': '1', 'actor1_name': 'Turo Pajala', 'actor1_gender': '0', 'actor2_name': 'Susanna Haavisto', 'actor2_gender': '0', 'actor3_name': 'Matti Pellonpää', 'actor3_gender': '2', 'actor4_name': 'Eetu Hilkamo','actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '4', 'director_name': 'Aki Kaurismäki', 'director_gender': '0', 'director_number': '1', 'producer_name': 'none', 'producer_number': '0', 'screeplay_name': 'Aki Kaurismäki', 'editor_name': 'Raija Talvio'})
    movies.append({'id': '2', 'actor1_name': 'Matti Pellonpää', 'actor1_gender': '2', 'actor2_name': 'Kati Outinen', 'actor2_gender': '1', 'actor3_name': 'Sakari Kuosmanen', 'actor3_gender': '2', 'actor4_name': 'Esko Nikkari', 'actor4_gender': '2', 'actor5_name': 'Kylli Köngäs', 'actor5_gender': '0', 'actor_number': '7', 'director_name': 'Aki Kaurismäki', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Mika Kaurismäki', 'producer_number': '1', 'screeplay_name': 'Aki Kaurismäki', 'editor_name': 'Raija Talvio'})
    movies.append({'id': '3', 'actor1_name': 'Tim Roth', 'actor1_gender': '2', 'actor2_name': 'Antonio Banderas', 'actor2_gender': '2', 'actor3_name': 'Jennifer Beals', 'actor3_gender': '1', 'actor4_name': 'Madonna', 'actor4_gender': '1', 'actor5_name': 'Marisa Tomei', 'actor5_gender': '1', 'actor_number': '24', 'director_name': 'Allison Anders', 'director_gender': '1', 'director_number': '4', 'producer_name': 'Lawrence Bender', 'producer_number': '1', 'screeplay_name': 'none', 'editor_name': 'Margaret Goodspeed'})
    movies.append({'id': '4', 'actor1_name': 'Emilio Estevez', 'actor1_gender': '2', 'actor2_name': 'Cuba Gooding Jr.', 'actor2_gender': '2', 'actor3_name': 'Denis Leary', 'actor3_gender': '2', 'actor4_name': 'Jeremy Piven', 'actor4_gender': '2', 'actor5_name': 'Peter Greene', 'actor5_gender': '2', 'actor_number': '15', 'director_name': 'Stephen Hopkins', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Gene Levy', 'producer_number': '1', 'screeplay_name': 'Lewis Colick', 'editor_name': 'Tim Wellburn'})
    movies.append({'id': '5', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0', 'actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'})
    return movies

@pytest.fixture
def lstmovies(movies):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,movies[i])    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0



def test_addFirst (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[2]




def test_addLast (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[1]
    movie = slt.lastElement(lst)
    assert movie == movies[2]




def test_getElement(lstmovies, movies):
    movie = slt.getElement(lstmovies, 1)
    assert book == movies[0]
    movie = slt.getElement(lstmovies, 5)
    assert movie == movies[4]



def test_removeFirst (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeFirst(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 1)
    assert movie  == movies[1]



def test_removeLast (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeLast(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (lst, movies):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, movies[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, movies[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, movies[2], 1)
    assert slt.size(lst) == 3
    movie = slt.getElement(lst, 1)
    assert movie == movies[2]
    movie = slt.getElement(lst, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    movie = {'id': '8', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0','actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'}
    print(slt.isPresent (lstmovies, movies[2]))
    assert slt.isPresent (lstmovies, movies[2]) > 0
    assert slt.isPresent (lstmovies, movie) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = slt.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[2]
    slt.deleteElement (lstmovies, pos)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[3]


def test_changeInfo (lstmovies):
    movie10 = {'id': '8', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0','actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'}
    slt.changeInfo (lstmovies, 1, movie10)
    movie = slt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    book1 = slt.getElement(lstmovies, 1)
    book5 = slt.getElement(lstmovies, 5)
    slt.exchange (lstmovies, 1, 5)
    assert slt.getElement(lstmovies, 1) == book5
    assert slt.getElement(lstmovies, 5) == book1
