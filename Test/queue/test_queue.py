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
from DataStructures import listiterator as it
from ADT import queue as q

list_type = 'ARRAY_LIST'

"""
   Creacion de diccionarios utilizados en las pruebas de la estructura de datos
"""
movie1={'id': '1', 'actor1_name': 'Turo Pajala', 'actor1_gender': '0', 'actor2_name': 'Susanna Haavisto', 'actor2_gender': '0', 'actor3_name': 'Matti Pellonpää', 'actor3_gender': '2', 'actor4_name': 'Eetu Hilkamo','actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '4', 'director_name': 'Aki Kaurismäki', 'director_gender': '0', 'director_number': '1', 'producer_name': 'none', 'producer_number': '0', 'screeplay_name': 'Aki Kaurismäki', 'editor_name': 'Raija Talvio'}
movie2={'id': '2', 'actor1_name': 'Matti Pellonpää', 'actor1_gender': '2', 'actor2_name': 'Kati Outinen', 'actor2_gender': '1', 'actor3_name': 'Sakari Kuosmanen', 'actor3_gender': '2', 'actor4_name': 'Esko Nikkari', 'actor4_gender': '2', 'actor5_name': 'Kylli Köngäs', 'actor5_gender': '0', 'actor_number': '7', 'director_name': 'Aki Kaurismäki', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Mika Kaurismäki', 'producer_number': '1', 'screeplay_name': 'Aki Kaurismäki', 'editor_name': 'Raija Talvio'}
movie3={'id': '3', 'actor1_name': 'Tim Roth', 'actor1_gender': '2', 'actor2_name': 'Antonio Banderas', 'actor2_gender': '2', 'actor3_name': 'Jennifer Beals', 'actor3_gender': '1', 'actor4_name': 'Madonna', 'actor4_gender': '1', 'actor5_name': 'Marisa Tomei', 'actor5_gender': '1', 'actor_number': '24', 'director_name': 'Allison Anders', 'director_gender': '1', 'director_number': '4', 'producer_name': 'Lawrence Bender', 'producer_number': '1', 'screeplay_name': 'none', 'editor_name': 'Margaret Goodspeed'}
movie4={'id': '4', 'actor1_name': 'Emilio Estevez', 'actor1_gender': '2', 'actor2_name': 'Cuba Gooding Jr.', 'actor2_gender': '2', 'actor3_name': 'Denis Leary', 'actor3_gender': '2', 'actor4_name': 'Jeremy Piven', 'actor4_gender': '2', 'actor5_name': 'Peter Greene', 'actor5_gender': '2', 'actor_number': '15', 'director_name': 'Stephen Hopkins', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Gene Levy', 'producer_number': '1', 'screeplay_name': 'Lewis Colick', 'editor_name': 'Tim Wellburn'}
movie5={'id': '5', 'actor1_name': 'none', 'actor1_gender': '0', 'actor2_name': 'none', 'actor2_gender': '0', 'actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '0', 'director_name': 'Timo Novotny', 'director_gender': '0', 'director_number': '1', 'producer_name': 'Timo Novotny', 'producer_number': '2', 'screeplay_name': 'Michael Glawogger', 'editor_name': 'Timo Novotny'}
movie6 = {'id': '6', 'actor1_name': 'Rita Lengyel', 'actor1_gender': '1', 'actor2_name': 'Milton Welsh', 'actor2_gender': '2', 'actor3_name': 'none', 'actor3_gender': '0', 'actor4_name': 'none', 'actor4_gender': '0', 'actor5_name': 'none', 'actor5_gender': '0', 'actor_number': '2', 'director_name': 'Marc Meyer', 'director_gender': '0', 'director_number': '2', 'producer_name': 'Marc Meyer', 'producer_number': '1', 'screeplay_name': 'none', 'editor_name': 'Marc Meyer'}
movie7 = {'id': '7', 'actor1_name': 'Mark Hamill', 'actor1_gender': '2', 'actor2_name': 'Harrison Ford', 'actor2_gender': '2', 'actor3_name': 'Carrie Fisher', 'actor3_gender': '1', 'actor4_name': 'Peter Cushing', 'actor4_gender': '2', 'actor5_name': 'Alec Guinness', 'actor5_gender': '2', 'actor_number': '106', 'director_name': 'George Lucas', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Gary Kurtz', 'producer_number': '2', 'screeplay_name': 'none', 'editor_name': 'Marcia Lucas'}
movie8 = {'id': '8', 'actor1_name': 'Albert Brooks', 'actor1_gender': '2', 'actor2_name': 'Ellen DeGeneres', 'actor2_gender': '1', 'actor3_name': 'Alexander Gould', 'actor3_gender': '2', 'actor4_name': 'Willem Dafoe', 'actor4_gender': '2', 'actor5_name': 'Brad Garrett', 'actor5_gender': '2', 'actor_number': '24', 'director_name': 'Andrew Stanton', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Graham Walters', 'producer_number': '1', 'screeplay_name': 'Andrew Stanton', 'editor_name': 'David Ian Salter'}
movie9 = {'id':'9', 'actor1_name': 'Tom Hanks', 'actor1_gender': '2', 'actor2_name': 'Robin Wright', 'actor2_gender': '1', 'actor3_name': 'Gary Sinise', 'actor3_gender': '2', 'actor4_name': 'Mykelti Williamson', 'actor4_gender': '2', 'actor5_name': 'Sally Field', 'actor5_gender': '1', 'actor_number': '67', 'director_name': 'Robert Zemeckis', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Wendy Finerman', 'producer_number': '3', 'screeplay_name': 'Eric Roth', 'editor_name': 'Arthur Schmidt'}
movie10 = {'id':'10', 'actor1_name': 'Kevin Spacey', 'actor1_gender': '2', 'actor2_name': 'Annette Bening', 'actor2_gender': '1', 'actor3_name': 'Thora Birch', 'actor3_gender': '1', 'actor4_name': 'Wes Bentley', 'actor4_gender': '2', 'actor5_name': 'Mena Suvari', 'actor5_gender': '1', 'actor_number': '41', 'director_name': 'Sam Mendes', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Bruce Cohen', 'producer_number': '2', 'screeplay_name': 'Alan Ball', 'editor_name': 'Christopher Greenbury'}
movie11 = {'id':'11', 'actor1_name': 'Orson Welles', 'actor1_gender': '2', 'actor2_name': 'Joseph Cotten', 'actor2_gender': '2', 'actor3_name': 'Dorothy Comingore', 'actor3_gender': '1', 'actor4_name': 'Ray Collins', 'actor4_gender': '2', 'actor5_name': 'George Coulouris', 'actor5_gender': '2', 'actor_number': '151', 'director_name': 'Orson Welles', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Orson Welles', 'producer_number': '2', 'screeplay_name': 'Orson Welles', 'editor_name': 'Robert Wise'}
movie12 = {'id':'12', 'actor1_name': 'Orson Welles', 'actor1_gender': '2', 'actor2_name': 'Joseph Cotten', 'actor2_gender': '2', 'actor3_name': 'Dorothy Comingore', 'actor3_gender': '1', 'actor4_name': 'Ray Collins', 'actor4_gender': '2', 'actor5_name': 'George Coulouris', 'actor5_gender': '2', 'actor_number': '151', 'director_name': 'Orson Welles', 'director_gender': '2', 'director_number': '1', 'producer_name': 'Orson Welles', 'producer_number': '2', 'screeplay_name': 'Orson Welles', 'editor_name': 'Robert Wise'}
movie13 = {'id':'13', 'book_title':'Title 13', 'author':'author 13'}
movie14 = {'id':'14', 'book_title':'Title 14', 'author':'author 14'}

def test_queueElements ():
    """
    Se prueba la creacion de una nueva cola, se agregan todos los datos creados por sistema y se imprime su valor
    """
    queue = q.newQueue(list_type)

    q.enqueue   (queue, movie5)
    q.enqueue   (queue, movie6)
    q.enqueue   (queue, movie3)
    q.enqueue   (queue, movie10)
    q.enqueue   (queue, movie1)
    q.enqueue   (queue, movie2)
    q.enqueue   (queue, movie8)
    q.enqueue   (queue, movie4)
    q.enqueue   (queue, movie7)
    q.enqueue   (queue, movie9)
    iterator = it.newIterator(queue)
    while  it.hasNext(iterator):
        element = it.next(iterator)
        result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
        print (result)

def test_sizeStack ():
    """
    Se prueba la creacion de una cola y la relacion con el tamaño al ingresar datos
    """
    
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))
    queue = q.newQueue(list_type)

    q.enqueue   (queue, book5)
    q.enqueue   (queue, book6)
    q.enqueue   (queue, book3)
    q.enqueue   (queue, book10)
    q.enqueue   (queue, book1)
    q.enqueue   (queue, book2)
    q.enqueue   (queue, book8)
    q.enqueue   (queue, book4)
    q.enqueue   (queue, book7)
    q.enqueue   (queue, book9)
    assert q.size(queue) ==10

def test_infoElements ():
    """
    Este test busca confirmar que los datos se almacenen de forma correcta y que
    sean los valores correctos en el orden apropiado de la estructura.
    """
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))
    queue = q.newQueue(list_type)

    q.enqueue   (queue, book5)
    q.enqueue   (queue, book6)
    q.enqueue   (queue, book3)
    q.enqueue   (queue, book10)
    q.enqueue   (queue, book1)
    q.enqueue   (queue, book2)
    q.enqueue   (queue, book8)
    q.enqueue   (queue, book4)
    q.enqueue   (queue, book7)
    q.enqueue   (queue, book9)
        
    elem = q.peek (queue)
    assert (q.size(queue) == 10)
    assert (elem == book5)
       
    elem = q.dequeue (queue)
    assert (q.size(queue) == 9)
    assert (elem == book5)

    elem = q.dequeue (queue)
    assert (q.size(queue) == 8)
    assert (elem == book6)

    elem = q.peek (queue)
    assert (q.size(queue) == 8 )
    assert (elem == book3)

    q.enqueue  (queue, book9)
    assert (q.size(queue) == 9)
    elem = q.peek ( queue)
    assert (elem == book3)
    
def test_peek_dequeue():
    """
    Este test prueba la creacion de una cola y que el orden de salida sea el correcto para la
    estructura en cuestion, y que el tamaño se reduzca para cada salida de objeto
    """

    queue = q.newQueue(list_type)
    assert q.size(queue) == 0
    assert q.isEmpty(queue)
    queue = q.newQueue(list_type)

    q.enqueue   (queue, book5)
    q.enqueue   (queue, book6)
    q.enqueue   (queue, book3)
    q.enqueue   (queue, book10)
    q.enqueue   (queue, book1)
    q.enqueue   (queue, book2)
    q.enqueue   (queue, book8)
    q.enqueue   (queue, book4)
    q.enqueue   (queue, book7)
    q.enqueue   (queue, book9)
    total = q.size(queue)
    while not (q.isEmpty(queue)):
        peek = q.peek(queue)
        assert(q.dequeue(queue) == peek)
        total-=1
        assert (total == q.size(queue))

def test_enqueue_dequeue():
    """
    Este test prueba que la cola pueda manejar inserciones y eliminaciones de forma correcta siguiendo
    un orden establecido, y que no quede referencia al objeto sacado despues de haberlo removido de la
    cola
    """
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))
     
    q.enqueue  (queue, book5)
    assert(q.size(queue) == 1)
    assert(q.peek(queue) ==q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue   (queue, book6)
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue   (queue, book3)
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue   (queue, book10)
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)

    q.enqueue   (queue, book1)
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)
        
    q.enqueue   (queue, book2)
    assert(q.size(queue) == 1)
    assert(q.peek(queue) == q.dequeue(queue))
    assert(q.size(queue) == 0)
              
    q.enqueue   (queue, book8)
    q.enqueue   (queue, book4)
    q.enqueue   (queue, book7)
    q.enqueue   (queue, book9)
       
    assert (q.size(queue) == 4)
    assert book8 == q.dequeue(queue)
    assert book4 == q.dequeue(queue)
    assert book7 == q.dequeue(queue)
    assert book9 == q.dequeue(queue)
   
    assert (q.size(queue)== 0)
        
def test_error_dequeue():
    """
    Este test busca comprobar que es imposible eliminar un objeto de una cola vacia
    """
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert(q.isEmpty(queue))
      
    with pytest.raises(Exception):
        q.dequeue(queue)

