from __init__ import *
nuevo(0,"inicio");
Nombre_lista_1 = ["linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 10"]
Nombre_lista_2 = ["columna 1","columna 2","columna 3","columna 4","columna 5","columna 6","columna 7","columna 8","columna 9","columna 10"]

#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aqui las precticas hechas
    pass
print(
    """\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║  ╔═════╗    ╔══════╗           ╗  ╔═══════╗  ╔═══╦═══╗   ╔═════╗   ╔═════╗  ║
║ ╔╝     ╚╗   ║      ╚╗          ║  ║              ║      ╔╝     ╚╗ ╔╝     ╚╗ ║
║ ║       ║   ║      ╔╝          ║  ║              ║      ║       ║ ║         ║
║ ║       ║   ╠═════╦╝           ║  ║              ║      ║       ║ ╚╗        ║
║ ║       ║   ║     ╚═╗          ║  ╠══════╝       ║      ║       ║  ╚═════╗  ║
║ ║       ║   ║       ║          ║  ║              ║      ║       ║        ╚╗ ║
║ ╚╗     ╔╝   ║     ╔═╝  ╚╗     ╔╝  ║              ║      ╚╗     ╔╝ ╚╗     ╔╝ ║
║  ╚═════╝    ╚═════╝     ╚═════╝   ╚═══════╝      ╩       ╚═════╝   ╚═════╝  ║
║                                                                             ║
║                                                                             ║
║                            ╔═════╗    ╔═══════╗   ╔═══╦═══╗                 ║
║                           ╔╝     ╚╗   ║               ║                     ║
║                           ║           ║               ║                     ║
║                           ╚╗          ║               ║                     ║
║                            ╚═════╗    ╠══════╝        ║                     ║
║                                  ╚╗   ║               ║                     ║
║                           ╚╗     ╔╝   ║               ║                     ║
║                            ╚═════╝    ╚═══════╝       ╩                     ║
║                                                                             ║
║                                                                             ║
║ ╔══════╗ ╔═════╗   ╔════╗  ╔══════╗  ╔══════╗  ╔═════╗    ╔══════╗  ╔══╦══╗ ║
║ ║        ║     ╚╗ ╔╝    ╚╗       ╔╝  ║        ╔╝     ╚╗   ║            ║    ║
║ ║        ║      ║ ║      ║      ╔╝   ║        ║           ║            ║    ║
║ ║        ║     ╔╝ ║      ║     ╔╝    ║        ╚╗          ║            ║    ║
║ ╠════╗   ╠══╦══╝  ║      ║   ╔═╝     ╠═════╝   ╚═════╗    ╠════╝       ║    ║
║ ║        ║  ╚╗    ║      ║  ╔╝       ║               ╚╗   ║            ║    ║
║ ║        ║   ╚═╗  ╚╗    ╔╝ ╔╝        ║        ╚╗     ╔╝   ║            ║    ║
║ ╩        ╩     ╚╝  ╚════╝  ╚═══════╝ ╚══════╝  ╚═════╝    ╚══════╝     ╩    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""");





pausa();limpiar();
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                           Python set /Array Methods                         ║
║                          ---------------------------                        ║
║                                                                             ║
║          Method           Description                                       ║
║                                                                             ║
║          add()            Adds an element to the set                        ║
║          clear()          Removes all the elements from the set             ║
║          copy()           Returns a copy of the set                         ║
║          difference()     Returns a set containing the difference between   ║
║                           two or more sets                                  ║
║          difference_update()  Removes the items in this set that are also   ║
║                           included in another, specified set                ║
║          discard()        Remove the specified item                         ║
║          intersection()   Returns a set, that is the intersection of two    ║
║                           or more sets                                      ║
║          intersection_update()    Removes the items in this set that are    ║
║                           not present in other, specified set(s)            ║
║          isdisjoint()     Try returns whether two sets have a intersection  ║
║          issubset()       Try eturns whether another set contains this set  ║
║          issuperset()     Try returns whether this set contains another set ║
║          pop()            Removes an element from the set                   ║
║          remove()         Removes the specified element                     ║
║          symmetric_difference()           Returns a set with the symmetric  ║
║                           differences of two sets                           ║
║          symmetric_difference_update()    inserts the symmetric differences ║
║                           from this set and another                         ║
║          union()          Return a set containing the union of sets         ║
║          update()         Update the set with another any iterable          ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                     Sets                                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
https://www.w3schools.com/python/python_ref_set.asp



conjunto1 = set('Python');                                  # define conj: P,y,t,h,o,n
conjunto2 = set('Pitonisa');                                # define conj: P,i,t,o,n,s,a
("-",conjunto2 - conjunto1)                                 # aplica diferencia: s, i, a
("|",conjunto1 | conjunto2)                                 # aplica unión: P,y,t,h,o,n,i,s,a
("&",conjunto1 & conjunto2)                                 # intersección: P,t,o,n
("^",conjunto1 ^ conjunto2)                                 # diferencia simétrica: y,h,i,s,a
""");



obj = {}

print (f"{obj}   {type(obj)}")
obj={0,4,5,2,6,"Ariel","chau 2022"}
print (f"{obj}   {type(obj)}")
obj_dic={0:"x",4:3,5:5,3:0,2:True,6:"Ariel","chau":"2022"}
obj_set={0,4,5,3,2,6,"chau"}
print (f"{obj_set}   {type(obj_set)}")
obj_list = list(obj_set)

print (f"{obj_list}   {type(obj_list)}")

lista = [5,3,6,3,5,8,9,6,5,3,6,5,6,7]
print (f"{lista}   {type(lista)}    {len(lista)}")

set_1 = {5,3,6,3,5,8,9,6,5,3,6,5,6,7}
print (f"{set_1}   {type(set_1)}    {len(set_1)}")
pausa();limpiar();
#################################################################
print("""
Descripción del método
add()                       Agrega un elemento al conjunto
clear()                     Elimina todos los elementos del conjunto
copy()                      Devuelve una copia del conjunto
difference()                Devuelve un conjunto que contiene la diferencia entre dos o más conjuntos
difference_update()         Elimina los elementos de este conjunto que también están incluidos en otro conjunto especificado
discard ()                  Eliminar el elemento especificado
intersection()              Devuelve un conjunto, que es la intersección de dos o más conjuntos
intersection_update()       Elimina los elementos de este conjunto que no están presentes en otro(s) conjunto(s) especificado(s)
isdisjoint()                Devuelve si dos conjuntos tienen una intersección o no
issubset()                  Devuelve si otro conjunto contiene este conjunto o no
issuperset()                Devuelve si este conjunto contiene otro conjunto o no
pop()                       Elimina un elemento del conjunto
remove()                    Elimina el elemento especificado
symmetric_difference()      Devuelve un conjunto con las diferencias simétricas de dos conjuntos
metric_difference_update()  inserta las diferencias simétricas de este conjunto y otro
union()                     Devuelve un conjunto que contiene la unión de conjuntos
update ()                   Actualizar el conjunto con otro conjunto, o cualquier otro iterable
""");
pausa();limpiar()
#################################################################
print("*"*104)
print("*","creación de sets/dicts".center(100),"*")
print("*"*104)
obj ={}
print (f"atención:\n{type(obj)}\n{obj=}")
obj={"dato1","dato2","dato3","dato4","dato5","dato6","dato7","dato8","dato9","dato10"}
print (f"atención:\n{type(obj)}\n{obj=}")

obj={"dato1":1,"dato2":2,"dato3":3,"dato4":4,"dato5":5,"dato6":6,"dato7":7,"dato8":8,"dato9":9,"dato10":10}
print (f"atención:\n{type(obj)}\n{obj=}")
pausa();limpiar()

#################################################################
print("*"*104)
print("*","len(set_)".center(100),"*")
print("*"*104)
print('''
Sets
    Set is a collection of items. 
    Let me take you back to your elementary or high school Mathematics lesson. 
    The Mathematics definition of a set can be applied also in Python. 
    Set is a collection of unordered and un-indexed distinct elements. 
    In Python set is used to store unique items, and it is possible to find the 
    _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _super set_ and _disjoint set_ among sets.
''')

st = {}
# or
st = set()
st = {'item1', 'item2', 'item3', 'item4'}
print(f"{len(st)=}")
#################################################################
print("¿Hay un item3 en el set? ", 'item3' in st) # Does set st contain item3? True
if 'item3' in st:
    print("sip")
else:
    print("no")
print("¿Hay un item5 en el set? ", 'item5' in st) # Does set st contain item3? True
if 'item5' in st:
    print("sip")
else:
    print("no")

#################################################################
print("*"*104)
print("*","union".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (f"union  {A.union(B)=}")
print (f"union  {B.union(A)=}")
print (f"union  {(A | B)=}")
print (f"union  {(B | A)=}")
#---------------------------------------------------------------
### Joining Sets
# ~ We can join two sets using the _union()_ or _update()_ method.
# ~ Union:  This method returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st_nuevo=st1.union(st2)
print(f"{st_nuevo=}")
st_nuevo=st2.union(st1)
print(f"{st_nuevo=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","update".center(100),"*")
print("*"*104)
### Update
# ~ This method inserts a set into a given set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
# ~ st2 contents are added to st1
print(f"{st1.update(st2)=}")
print(f"{st2.update(st1)=}") 
pausa();limpiar()
#################################################################
print("*"*104)
print("*","difference_update".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (f"A.difference_update(B) {A.difference_update(B)=}")
print (f"B.difference_update(A) {B.difference_update(A)=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","intersección".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (f"intersección  {A.intersection(B)=}")
print (f"intersección  {B.intersection(A)=}")
print (f"intersección  {(A & B)=}")
print (f"intersección  {(B & A)=}")
#---------------------------------------------------------------
### Finding Intersection Items
# ~ Intersection returns a set of items which are in both the sets. See the example
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(f"{st1.intersection(st2)=}")
print(f"{st2.intersection(st1)=}")
#---------------------------------------------------------------
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(f"{whole_numbers.intersection(even_numbers)=}")
print(f"{even_numbers.intersection(whole_numbers)=}")
#---------------------------------------------------------------
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(f"{python.intersection(dragon) =}")
print(f"{dragon.intersection(python)=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","add".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
print (f"original {A=}")
print (f"add 1 {A.add(1)=}")
#---------------------------------------------------------------
### Adding Items to a Set
# ~ Once a set is created we cannot change any items and we can also add additional items.
st = {'item1', 'item2', 'item3', 'item4'}
print(f"original:{(st)=}")
print(f"{st.add('item5')=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","difference".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (f"difference  {A.difference(B)=}")
print (f"difference  {B.difference(A)=}")
print (f"difference  {(A - B)=}")
print (f"difference  {(B - A)=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","remove".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
print (f"A.remove(10)  {A.remove(10)}") 
pausa();limpiar()
#---------------------------------------------------------------
# ~ If the item is not found _remove()_ method will raise errors, so it is good to check 
# ~ if the item exist in the given set. However, _discard()_ method doesn't raise any errors.
#---------------------------------------------------------------
st = {'item1', 'item2', 'item3', 'item4'}
print(f"original:{(st)=}")
print(f"{st.remove('item2')=}")
#---------------------------------------------------------------
print(f"original:{(st)=}")
try: 
    print(f"{st.remove('item5')=}")
except Exception as error:
    print (f"error del tipo {error}")

pausa();limpiar()
#################################################################
print("*"*104)
print("*","discard".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
print (f"original {A=}")
# Discarding element from the set
print (f"A.discard(30)  {A.discard(30)=}")
#---------------------------------------------------------------
st = {'item1', 'item2', 'item3', 'item4'}
print(f"original:{(st)=}")
print(f"{st.discard('item2')=}")
#---------------------------------------------------------------
print(f"original:{(st)=}")
print(f"{st.discard('item5')=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","clear".center(100),"*")
print("*"*104)
A.clear()
print (f"clear  {A=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","update".center(100),"*")
#################################################################
print("*"*104)
print("*","pop".center(100),"*")
print("*","No encuentro utilidade de este metodo:(".center(100),"*")
print("*"*104)
A = {10, 20, 30, 40, 80}
print (f"original {A=}")
# elimina un objeto randomm
print (f"pop  {A.pop()=}")
print (f"pop  {A.pop()=}")
print (f"pop  {A.pop()=}")
print (f"final {A=}")
# ~ The pop() methods remove a random item from a list and it returns the removed item.
# ~ la utilidad de este método se me escapa
st = {'item1', 'item2', 'item3', 'item4'}
print(f"original:{(st)=}")
st.pop()  # removes a random item from the set
# ~ cual
item_eliminado = st.pop() 
print(f"{item_eliminado=}")
print(f"final:{(st)=}")
pausa();limpiar()
#################################################################
print("*"*104)
print("*","clear".center(100),"*")
print("*"*104)
### Clearing Items in a Set
# ~ If we want to clear or empty the set we use _clear_ method.
# ~ no elimina la coleccion, solo la vacia
st = {'item1', 'item2', 'item3', 'item4'}
print(f"original:{(st)=}")
st.clear()
print(f"final:{(st)=}")
#################################################################
print("*"*104)
print("*","difference_update".center(100),"*")
print("*"*104)
### Deleting a Set
# ~ If we want to delete the set itself we use _del_ operator.
st = {'item1', 'item2', 'item3', 'item4'}
del st
try:
    print(f"final:{(st)=}")
except Exception as error:
    print(f"Error\n no existe st{error=} ")
#################################################################
print("*"*104)
print("*","de lista a set".center(100),"*")
print("*"*104)
### Converting List to Set
# ~ We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
#################################################################
print("*"*104)
print("*","Subset: _issubset()_".center(100),"*")
print("*","Super set: _issuperset_".center(100),"*")
print("*"*104)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(f"{st1.issubset(st2)=}")
print(f"{st2.issubset(st1)=}")
print(f"{st1.issuperset(st2)=}")
print(f"{st2.issuperset(st1)=}")
#---------------------------------------------------------------
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(f"{whole_numbers.issubset(even_numbers)=}")# 
print(f"{even_numbers.issubset(whole_numbers)=}")# 
#---------------------------------------------------------------
print(f"{whole_numbers.issuperset(even_numbers)=}") # 
print(f"{even_numbers.issuperset(whole_numbers)=}") # 

#---------------------------------------------------------------
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(f"{python.issubset(dragon)=}")       
print(f"{dragon.issubset(python)=}")       
#---------------------------------------------------------------
print(f"{python.issuperset(dragon)=}")       
print(f"{dragon.issuperset(python)=}")     
#################################################################
print("*"*104)
print("*","difference".center(100),"*")
print("*"*104)
### Checking the Difference Between Two Sets
# ~ It returns the difference between two sets.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(f"{st2.difference(st1)=}")   
print(f"{st1.difference(st2)=}")  
#---------------------------------------------------------------  
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(f"{whole_numbers.difference(even_numbers)=}") #{1, 3, 5, 7, 9}
print(f"{even_numbers.difference(whole_numbers)=}")
#---------------------------------------------------------------
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(f"{python.difference(dragon)=}")     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets  
print(f"{dragon.difference(python)=}")     # {'d', 'r', 'a', 'g'}
#################################################################
print("*"*104)
print("*","symmetric_difference".center(100),"*")
print("*"*104)
### Finding Symmetric Difference Between Two Sets
# ~ It returns the the symmetric difference between two sets. 
# ~ means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
print(f"{st2.symmetric_difference(st1)=}")   
print(f"{st1.symmetric_difference(st2)=}")  
#---------------------------------------------------------------
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
# {0, 6, 7, 8, 9, 10}
print(f"{whole_numbers.symmetric_difference(some_numbers)=}")   
print(f"{some_numbers.symmetric_difference(whole_numbers)=}") 
#---------------------------------------------------------------
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(f"{python.symmetric_difference(dragon)=}")   
print(f"{dragon.symmetric_difference(python)=}") 
#################################################################
print("*"*104)
print("*","isdisjoint".center(100),"*")
print("*"*104)
### Joining Sets
# ~ If two sets do not have a common item or items we call them disjoint sets.
# ~ We can check if two sets are joint or disjoint using _isdisjoint()_ method.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
print(f"{st2.isdisjoint(st1)=}")   
print(f"{st1.isdisjoint(st2)=}")
#---------------------------------------------------------------
odd_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
print(f"{odd_numbers.isdisjoint(even_numbers)=}")   
print(f"{even_numbers.isdisjoint(odd_numbers)=}")
#---------------------------------------------------------------
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
print(f"{python.isdisjoint(dragon)=}")   
print(f"{dragon.isdisjoint(python)=}") 
#################################################################
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

'''
### Exercises: Level 1
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard

### Exercises: Level 2
1. Join A and B
1. Find A intersection B
1. Is A subset of B
1. Are A and B disjoint sets
1. Join A with B and B with A
1. What is the symmetric difference between A and B
1. Delete the sets completely

### Exercises: Level 3
1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
1. Explain the difference between the following data types: string, list, tuple and set
2.  _I am a teacher and I love to inspire and teach people.
    _ How many unique words have been used in the sentence? 
    Use the split methods and set to get the unique words.
'''


