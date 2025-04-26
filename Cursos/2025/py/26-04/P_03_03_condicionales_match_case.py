from __init__ import *
limpiar()
print(Back.GREEN+"""\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║  ╔═════╗  ╔════╗  ╔╗      ╦ ╔═════╗  ╦  ╔════╗  ╦   ╔════╗                  ║
║ ╔╝       ╔╝    ╚╗ ║╚╗     ║ ║     ╚╗ ║ ╔╝    ╚╗ ║  ╔╝    ╚╗                 ║
║ ║        ║      ║ ║ ╚╗    ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ║        ║      ║ ║  ╚╗   ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ║        ║      ║ ║   ╚╗  ║ ║      ║ ║ ║        ║  ║      ║ ╠═════╝         ║
║ ║        ║      ║ ║    ╚╗ ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ╚╗       ╚╗    ╔╝ ║     ╚╗║ ║     ╔╝ ║ ╚╗    ╔╝ ║  ╚╗    ╔╝                 ║
║  ╚════╝   ╚════╝  ╩      ╚╝ ╚═════╝  ╩  ╚════╝  ╩   ╚════╝                  ║
║                                                                             ║
║                                                                             ║
║                           ╔╗      ╦   ╔════╗  ╦         ╔══════╗  ╔════╗    ║
║                           ║╚╗     ║  ╔╝    ╚╗ ║         ║        ╔╝    ╚╗   ║
║                           ║ ╚╗    ║  ║      ║ ║         ║        ║          ║
║                           ║  ╚╗   ║  ║      ║ ║         ║        ╚╗         ║
║                           ║   ╚╗  ║  ╠══════╣ ║         ╠═════╝   ╚════╗    ║
║                           ║    ╚╗ ║  ║      ║ ║         ║              ╚╗   ║
║                           ║     ╚╗║  ║      ║ ║         ║        ╚╗    ╔╝   ║
║                           ╩      ╚╝  ╩      ╩ ╚══════╝  ╚══════╝  ╚════╝    ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
╠═════════════════════════════════════════════════════════════════════════════╣"""+Back.RESET+"""
║                                                                             ║
║                                                                             ║
║    ╔╗      ╔╗   ╔═════╗    ╔═══╦═══╗   ╔═════╗     ╦       ╦                ║
║    ║╚╗    ╔╝║  ╔╝     ╚╗       ║      ╔╝     ╚╗    ║       ║                ║
║    ║ ╚╗  ╔╝ ║  ║       ║       ║      ║            ║       ║                ║
║    ║  ╚╗╔╝  ║  ║       ║       ║      ║            ║       ║                ║
║    ║   ╚╝   ║  ╠═══════╣       ║      ║            ╠═══════╣                ║
║    ║        ║  ║       ║       ║      ║            ║       ║                ║
║    ║        ║  ║       ║       ║      ╚╗     ╔╝    ║       ║                ║
║    ╩        ╩  ╩       ╩       ╩       ╚═════╝     ╩       ╩                ║
║                                                                             ║
║                                                                             ║
║                        ╔═════╗      ╔═════╗       ╔═════╗      ╔══════╗     ║
║                       ╔╝     ╚╗    ╔╝     ╚╗     ╔╝     ╚╗     ║            ║
║                       ║            ║       ║     ║             ║            ║
║                       ║            ║       ║     ╚╗            ║            ║
║                       ║            ╠═══════╣      ╚═════╗      ╠═════╝      ║
║                       ║            ║       ║            ╚╗     ║            ║
║                       ╚╗     ╔╝    ║       ║     ╚╗     ╔╝     ║            ║
║                        ╚═════╝     ╩       ╩      ╚═════╝      ╚══════╝     ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝"""+Back.RESET)
def ya_hechos():
    pass
char= input("ingrese su ocpción (Y o N )").title()
match char:
    case 'Y':
        print('Yes')
    case 'N':
        print('No')
    case other:
        print('opcion no válida')

print ("*"*100)
#################################################################################################
numero=int(input("ingrese su ocpción (1 o 2) "))
match numero:
    case 1:
        print('uno')
    case 2:
        print('dos')
    case other:
        print('sin datos')

print ("*"*100)
#################################################################################################
opcion = input("ingrese su ocpción (Archivo,Buscar,Cargar o Pegar) ").title()

match opcion:
    case 'Archivo':
        print('opcion Archivo')
    case 'Buscar':
        print('opcion Buscar')
    case 'Cargar':
        print('opcion Cargar')
    case 'Pegar':
        print('opcion Pegar')
    case other:
        print('opcion no válida')
        
        
        
# ~ file_handler_v2('remove --ask file1.txt file2.jpg file3.pdf')
# ~ Please confirm: Removing files: ['file1.txt', 'file2.jpg', 'file3.pdf']
 
# ~ file_handler_v2('delete file1.txt file2.jpg file3.pdf')
# ~ Removing files: ['file1.txt', 'file2.jpg', 'file3.pdf']  
# ~ match command.split():
    # ~ case ['show']:
        # ~ print('List all files and directories: ')
        # ~ # code to list files
    # ~ case ['remove' | 'delete', *files] if '--ask' in files:
        # ~ del_files = [f for f in files if len(f.split('.'))>1]
        # ~ print('Please confirm: Removing files: {}'.format(del_files))
        # ~ # code to accept user input, then remove files
    # ~ case ['remove' | 'delete', *files]:
        # ~ print('Removing files: {}'.format(files))
        # ~ # code to remove files
    # ~ case _:
        # ~ print('Command not recognized')       

# First, ask the player about their CPU
cpuModel = str.lower(input("Please enter your CPU model: "))
 
# The match statement evaluates the variable's value
match cpuModel:
    case "celeron": # We test for different values and print different messages
            print ("Forget about it and play Minesweeper instead...")
    case "core i3":
            print ("Good luck with that ;)")
    case "core i5":
            print ("Yeah, you should be fine.")
    case "core i7":
            print ("Have fun!")
    case "core i9":
            print ("Our team designed nice loading screens… Too bad you won't see them...")
    case _: # the underscore character is used as a catch-all.
            print ("Is that even a thing?")

print ("*"*100)
#################################################################################################
from http import HTTPStatus
import random

http_status = random.choice(list(HTTPStatus))

match http_status:
    case 200 | 201 | 204 as status:#or
        # 👆 Using "as status" extracts its value
        print(f"Everything is good! {status = }") # 👈 Now status can be used inside handler

    case 400 | 404 as status:
        print(f"You did something wrong! {status = }")

    case 500 as status:
        print(f"Oops... Is the server down!? {status = }")

    case _ as status:
        print(f"No clue what to do with {status = }!")

print ("*"*100)
#################################################################################################     
baskets = [
    ["apple", "pear", "banana"], # 🍎 🍐 🍌
    ["chocolate", "strawberry"], # 🍫 🍓
    ["chocolate", "banana"], # 🍫 🍌
    ["chocolate", "pineapple"], # 🍫 🍍
    ["apple", "pear", "banana", "chocolate"], # 🍎 🍐 🍌 🍫
]

def resolve_basket(basket: list):
    match basket:

        # 👇 Matches any 3 items
        case [i1, i2, i3]: # 👈 These are extracted as vars and used here 👇
            print(f"Wow, your basket is full with: '{i1}', '{i2}' and '{i3}'")

        # 👇 Matches >= 4 items
        case [_, _, _, *_] as basket_items:
            print(f"Wow, your basket has so many items: {len(basket_items)}")

        # 👇 2 items. First should be 🍫, second should be 🍓 or 🍌
        case ["chocolate", "strawberry" | "banana"]:
            print("This is a superb combination. 🍫 + 🍓|🍌")

        # 👇 2 items. First should be 🍫, second should be 🍍
        case ["chocolate", "pineapple"]:
            print("Eww, really? 🍫 + 🍍 = ?")

        # 👇 Any amount of items starting with 🍫
        case ["chocolate", *_]:
            print("I don't know what you plan but it looks delicious. 🍫")

        # 👇 If nothing matched before
        case _:
            print("Don't be cheap, buy something else")


for basket in baskets:
    print(f"📥 {basket}")
    resolve_basket(basket)
    print()

print ("*"*100)
#################################################################################################            
mappings: list[dict[str, str | int]] = [
    {"name": "Gui Latrova", "twitter_handle": "@guilatrova"},
    {"name": "John Doe"},
    {"name": "JOHN DOE"},
    {"name": 123456},
    {"full_name": "Peter Parker"},
    {"full_name": "Peter Parker", "age": 16}
]

def resolve_mapping(mapping: dict[str|int]):
    match mapping:
        # 👇 Matches any
        #    (1) "name" AND any (2) "twitter_handle"
        case {"name": name, "twitter_handle": handle}:
            print(f"😉 Make sure to follow {name} at {handle} to keep learning") # 😉 This is good advice

        # 👇 Matches any
        #    (1) "name" (2) if val is str and (3) it's all UPPER CASED
        case {"name": str() as name} if name == name.upper():
            print(f"😥 Hey, there's no need to shout, {name}!")

        # 👇 Matches any
        #    (1) "name" (2) if val is str. It will fall here whenever the above 👆 doesn't match
        case {"name": str() as name}:
            print(f"👋 Hi {name}!")

        # 👇 Matches any
        #    (1) "name" (2) if val is int.
        case {"name": int()}:
            print("🤖 Are you a robot or what? How can I say your name? ")

        # 👇 Matches any
        #    (1) "full_name" (2) and NOTHING else
        case {"full_name": full_name, **remainder} if not remainder:
            print(f"Thanks mr/ms {full_name}!")

        # 👇 Matches any
        #    (1) "full_name" (2) and ANYTHING else
        case {"full_name": full_name, **remainder}:
            print(f"Just your full name is fine! No need to share {list(remainder.keys())}")

print ("*"*100)
#################################################################################################

for mapping in mappings:
    print(f"📥 {mapping}")
    resolve_mapping(mapping)
    print()
    
from dataclasses import dataclass

@dataclass
class Move:
    x: int # horizontal
    y: int # vertical

@dataclass
class Action:
    name: str

@dataclass
class UnknownStep:
    random_value = "Darth Vader riding a monocycle"


steps = [
    Move(1, 0),
    Move(2, 5),
    Move(0, 5),
    Action("Work"),
    Move(0, 0),
    Action("Rest"),
    Move(0, 0),
    UnknownStep(),
    Action("End"),
]


def resolve_step(step):
    match step:
        # 👇 Match any action that has name = "End"
        case Action(name="End"): # 👈 Note we're not instantiating anything
            print("🔚 Flow finished")

        # 👇 Match any Action type
        case Action():
            print("👏 Good to see you're doing something")

        # 👇 Match any Move with x,y == 0,0
        case Move(0, 0):
            print("💂 You're not really moving, stop pretending")

        # 👇 Match any Move with y = 0
        case Move(x, 0):
            print(f"➡️ You're moving horizontally to {x}")

        # 👇 Match any Move with x = 0
        case Move(0, y):
            print(f"🔝 You're moving vertically to {y}")

        # 👇 Match any Move type
        case Move(x, y):
            print(f"🗺️ You're moving to ({x}, {y})")

        # 👇 When nothing matches
        case _:
            print(f"❓ I've got not idea what you're doing")



for step in steps:
    print(f"📥 {step}")
    resolve_step(step)
    print()

print ("*"*100)
#################################################################################################
values=[]
while len(values)<10:
        
    # Matching structure in Python switch-case
    match values:
        case [a]:
            print(f'Only one item: {a}')
        case [a, b]:
            print(f'Two items: {a}, {b}')
        case [a, b, c]:
            print(f'Three items: {a}, {b}, and {c}')
        case [a, b, c, *rest]:
            print(f'More than three items: {a}, {b}, {c}, as well as: {rest}')
    values.append("a")

print ("*"*100)
#################################################################################################
def type_of(var):
    match var:
        case int() | float() as var:
            return "Number"
        case dict() as var:
            return "Dictionary"
        case list() | tuple()  as var:
            return "List, tuple, or set"
        case set() as var:
            return "List, tuple, or set"
        case str() as var:
            return "String"
        case _: #case other: 
            return "Something else"
import datetime
ahora = datetime.datetime.now()
print(f"{type_of('Hola')=}")
print(f"{type_of(3)=}")
print(f"{type_of([1,2,3,2,1])=}")
print(f"{type_of((1,2,3,2,1))=}")
print(f"{type_of({1,2,3,2,1})=}")
print(f"{type_of({'A':2,'B':2})=}")
print(f"{type_of(ahora)=}")

print ("*"*100)
#################################################################################################
def award(student):
    match student:
        case {'name': name, 'courses': courses, 'grade': grade} if courses > 15 and grade >= 90:
            return f"{name}: Exceptional"
        case {'name': name, 'courses': courses, 'grade': grade} if grade >= 90:
            return f"{name}: Future star"
        case _:
            return f"{name}: No current award"



print(award({'name': 'Kate', 'grade':90, 'courses':16}))
print(award({'name': 'Jane', 'grade':90, 'courses':6}))
print(award({'name': 'Jane', 'grade':0, 'courses':0}))


print ("*"*100)
#################################################################################################
def calc(n:int):
    return (n**2)
 
def calc(n:float):
    return (n**3)  
def is_(n):
    is_int = isinstance(n, int)

    match is_int:
        case True : print(f"Square of {n} is:",calc(n))
        case False : print(f"Cube of {n} is:", calc(n))
is_(n = 8)
is_(n = 3.14159)


print ("*"*100)
#################################################################################################
n = 0
match n:
    case n if n < 0:
        print("Number is negative")
    case n if n == 0:
        print("Number is zero")
    case n if n > 0:
        print("Number is positive")

print ("*"*100)
#################################################################################################
score = 84
match score:
    case score if score >= 90:
        print('A')
    case score if score >= 80:
        print('B')
    case score if score >= 70:
        print('C')
    case score if score >= 60:
        print('D')
    case _:
        print('F')
# Output: B
