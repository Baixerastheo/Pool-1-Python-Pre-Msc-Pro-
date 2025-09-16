# ====== 1.1 ======

li = ["Bonjour", 5, "je suis", 18.5, "un fdp"]


# ====== 1.2 ======

element = li[4]
print(element)

# ====== 1.3 ======

li.append(42)
number = "forty-two"
li.append(number)
print(li)

# ====== 1.4 ======

for item in li:
    print(item)

# ====== 1.5 ======

delete_element = li.pop()
print(delete_element)
print(li)

# ====== 1.6 ======

first_element = li.insert(0, 1)
print(first_element)

# ====== 1.7 ======

[print(item) for item in li[1:4]]

# ====== 1.8 ======

li.reverse()
print(li)

# ====== 1.9 ======

one_two = li[::2]
print(one_two)

# ====== 1.10 ======

my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
# regroupe les éléments de la deuxième liste à la première grâce à la méthode extend

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]
# même principe mais sans méthode

# ====== 2.1 ======
from functools import reduce
import operator


def multiply(liste):
    r = 1
    for item in liste:
        r *= item
    return r


lst = [1, 2, 3, 4, 5]
print(multiply(lst))

# ====== 2.2 ======

listTen = [x + 10 for x in [3, 2, 6, 7, 1, 4]]
# Parcours tous les éléments de la liste en additionnant chacun des indices par 10
print(listTen)

# ====== 2.3 ======

print(
    list(filter(lambda x: x > 10, [42, 3, 4, 7]))
)  # affiche le nombre de la liste si ce dernier est supérieur à 10

# ====== 2.4 ======

lst = [42, 50, 1, 102, 10]

minNum = min(lst)
biggestNum = max(lst)

print(minNum, biggestNum)

# ====== 2.5 ======

print(lst[::-1])

# ====== 2.6 ======

print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
# divise par 2 un élément de la liste si ce dernier est pair sinon il est multiplié par 2

# ====== 2.7 ======

print([*enumerate([42, 3, 4, 18, 3, 10])])
# donne la position de chaque élément dans la liste ex : 42 est à la position 0

# ====== 2.8 ======

# en fonction de la position qu'on print, il va associer un prénom à un nom
first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
print(magic[0])  # prend le premier élément jackie et le dernier élément " chan "
print(
    magic[3]
)  # prend le dernier élément " Sylvester " et le dernier élément " stallone "
print(magic[1][0])  # prend le premier élément "Jackie"
print(magic[0][1])  # prend le dernier élément " Chan "
print(magic[2])  # #Arnold Schwarzenegger

# ====== Challenges ======

import random

n = 1000000
li = [random.randint(1, 10) for _ in range(n)]

print(sorted(li))

# ====== 3.1 ======
player_key = input("Enter a player's name: ")
player_team = input("Enter a player's team: ")

student = {
    "name": player_key,
    "team": player_team,
}

print(student)

# ====== 3.2 ======

superheroes = {
    "Batman": {
        "id": 1,
        "aliases": ["Bruce Wayne", "Dark Knight"],
        "location": {
            "number": 1007,
            "street": "Mountain Drive",
            "city": "Gotham"
        }
    },
    "Superman": {
        "id": 2,
        "aliases": ["Kal-El", "Clark Kent", "The Man of Steel"],
        "location": {
            "number": 344,
            "street": "Clinton Street",
            "apartment": "3D",
            "city": "Metropolis"
        }
    }
}

print(superheroes["Superman"]["location"]["city"])

# ====== 3.3 ======

superheroes["Batman"]["aliases"].append("Caped Crusader")

print(superheroes["Batman"]["aliases"])

# ====== 3.4 ======

d = {
    "dalmatians": 101,
    "pi": 3.14,
    "beast": 3*2*111,
    "life": 42,
    "googol": 10**100
}

max_key = max(d, key=d.get)
print(max_key)

# ====== 4.1 ======

guests = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

name = input("Enter your name: ")

if name in guests:
    print("welcome in")
else:
    print("get lost!")

# ====== 4.2 ======

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 1, 2, 2, 3]))
print(remove_duplicates(['a', 2, 'a', 2, 'A']))

# ====== 4.3 ======

# Chaque réunion est une liste contenant le jour et l'heure et les participants
meetings = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"]
]

name = input("Entrez le nom du participant : ")

# Parcourir toutes les réunions
for meeting in meetings:
    day = meeting[0]              # Extraire le jour de la réunion
    time = meeting[1]             # Extraire l'heure de la réunion
    participants = meeting[2:]    # Extraire tous les participants

    # Vérifier si le nom saisi est dans la liste des participants
    if name in participants:
        print(f"{name} a une réunion le {day} à {time}")