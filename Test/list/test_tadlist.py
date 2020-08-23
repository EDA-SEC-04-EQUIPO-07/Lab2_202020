"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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


import pytest 
import config 


from ADT import list as lt



def cmpfunction (element1, element2):
    if element1['id'] == element2['id']:
        return 0
    elif element1['id'] < element2['id']:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    # lst = lt.newList('SINGLE_LINKED', cmpfunction)
    lst = lt.newList('ARRAY_LIST', cmpfunction)
    return lst


@pytest.fixture
def movies ():
    movies = []
    movies.append({'id': '1', 'actor1_name': 'Turo Pajala', 'actor1_gender': '0', 'actor2_name': 'Susanna Haavisto', 'actor2_gender': '0', 'actor3_name': 'Matti Pellonpää', 'actor3_gender': '2', 'actor4_name': 'Eetu Hilkamo','actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '4', 'director_name': 'Aki Kaurismäki', 'director_gender': '0', 'director_number': '1', 'producer_name': 'none', 'producer_number': '0', 'screeplay_name': 'Aki Kaurismäki', 'editor_name': 'Raija Talvio'})
    movies.append({'id': '2', 'actor1_name': 'Matti Pellonpää', 'actor1_gender': '2', 'actor2_name': 'Kati Outinen', 'actor2_gender': '1', 'actor3_name': 'Sakari Kuosmanen', 'actor3_gender': '2', 'actor4_name': 'Esko Nikkari', 'actor4_gender': '2', 'actor5_name': 'Kylli Köngäs', 'actor5_gender': '0', 'actor_number': '7', 'director_name': 'Aki Kaurismäki', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Mika Kaurismäki', 'producer_number': '1', 'screeplay_name': 'Aki Kaurismäki', 'editor_name': 'Raija Talvio'})
    movies.append({'id': '3', 'actor1_name': 'Tim Roth', 'actor1_gender': '2', 'actor2_name': 'Antonio Banderas', 'actor2_gender': '2', 'actor3_name': 'Jennifer Beals', 'actor3_gender': '1', 'actor4_name': 'Madonna', 'actor4_gender': '1', 'actor5_name': 'Marisa Tomei', 'actor5_gender': '1', 'actor_number': '24', 'director_name': 'Allison Anders', 'director_gender': '1', 'director_number': '4', 'producer_name': 'Lawrence Bender', 'producer_number': '1', 'screeplay_name': 'none', 'editor_name': 'Margaret Goodspeed'})
    movies.append({'id': '4', 'actor1_name': 'Emilio Estevez', 'actor1_gender': '2', 'actor2_name': 'Cuba Gooding Jr.', 'actor2_gender': '2', 'actor3_name': 'Denis Leary', 'actor3_gender': '2', 'actor4_name': 'Jeremy Piven', 'actor4_gender': '2', 'actor5_name': 'Peter Greene', 'actor5_gender': '2', 'actor_number': '15', 'director_name': 'Stephen Hopkins', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Gene Levy', 'producer_number': '1', 'screeplay_name': 'Lewis Colick', 'editor_name': 'Tim Wellburn'})
    movies.append({'id': '5', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0', 'actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'})
    print (movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    lst = lt.newList('ARRAY_LIST', cmpfunction)
    # lst = lt.newList('SINGLE_LINKED', cmpfunction)
    for i in range(0,5):    
        lt.addLast(lst,movies[i])    
    return lst


def test_empty (lst):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0




def test_addFirst (lst, movies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addFirst (lst, movies[1])
    assert lt.size(lst) == 1
    lt.addFirst (lst, movies[2])
    assert lt.size(lst) == 2
    book = lt.firstElement(lst)
    assert book == movies[2]




def test_addLast (lst, movies):
    assert lt.isEmpty(lst) == True
    assert lt.size(lst) == 0
    lt.addLast (lst, movies[1])
    assert lt.size(lst) == 1
    lt.addLast (lst, movies[2])
    assert lt.size(lst) == 2
    movie = lt.firstElement(lst)
    assert movie == movies[1]
    movie = lt.lastElement(lst)
    assert movie == movies[2]




def test_getElement(lstmovies, movies):
    movie = lt.getElement(lstmovies, 1)
    assert movie == movies[0]
    movie = lt.getElement(lstmovies, 5)
    assert movie == movies[4]




def test_removeFirst (lstmovies, movies):
    assert lt.size(lstmovies) == 5
    lt.removeFirst(lstmovies)
    assert lt.size(lstmovies) == 4
    movie = lt.getElement(lstmovies, 1)
    assert movie  == movies[1]



def test_removeLast (lstmovies, movies):
    assert lt.size(lstmovies) == 5
    lt.removeLast(lstmovies)
    assert lt.size(lstmovies) == 4
    movie = lt.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (lst, movies):
    assert lt.isEmpty(lst) is True
    assert lt.size(lst) == 0
    lt.insertElement (lst, movies[0], 1)
    assert lt.size(lst) == 1
    lt.insertElement (lst, movies[1], 2)
    assert lt.size(lst) == 2
    lt.insertElement (lst, movies[2], 1)
    assert lt.size(lst) == 3
    movie = lt.getElement(lst, 1)
    assert movie == movies[2]
    movie = lt.getElement(lst, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    movie = {'id': '8', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0','actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'}
    assert lt.isPresent (lstmovies, movies[2]) > 0
    assert lt.isPresent (lstmovies, movie) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = lt.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = lt.getElement(lstmovies, pos)
    assert movie == movies[2]
    lt.deleteElement (lstmovies, pos)
    assert lt.size(lstmovies) == 4
    movie = lt.getElement(lstmovies, pos)
    assert movie == movies[3]



def test_changeInfo (lstmovies):
    movie10 = {'id': '8', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0','actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'}
    lt.changeInfo (lstmovies, 1, movie10)
    movie = lt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie1 = lt.getElement(lstmovies, 1)
    movie5 = lt.getElement(lstmovies, 5)
    lt.exchange (lstmovies, 1, 5)
    assert lt.getElement(lstmovies, 1) == movie5
    assert lt.getElement(lstmovies, 5) == movie1
