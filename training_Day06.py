# ====== 1.1 ======

def f1 () :
    return 42

def f2(x):
    return 2 * x
print (f1 () ) # retourne 42
print (f2 (5) + f1 () ) # retourne 2 * 5 + 42 = 52

# ====== 1.2 ======

def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print(" ============ ")

bread()
lettuce()
tomato()
ham()
ham()
bread()

# ====== 1.3 ======

def sandwich ():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

for _ in range(4):
    sandwich()

# ====== 1.4 ======

def order():
    user_input = input("Nombre de sandwich : ")
    try:
        sandwich_order = int(user_input)
        # Vérifie que c'est strictement positif
        if sandwich_order <= 0:
            print("I can't do this !")
            return
    except ValueError:
        print("I can't do this !")
        return

    for _ in range(sandwich_order):
        sandwich()

print(order())

# ====== 4.3 ======



# ====== Challenge ======


def chrono_pow(base, exp):
    result = base ** exp
    print(f"{base}^{exp} ")
    return result

chrono_pow(42, 84)
chrono_pow(42, 168)


# ====== 2.1 ======

def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1) # ex : 42 - 1 = 41 donc 42 + 41 + 40 ...

result = recursive_sum(42)
print(result)

# ====== 2.2 ======

import string

def is_palindrome():
    texte = input("Entrez une chaîne : ")

    # supprime espaces et ponctuation, met en minuscules
    texte_nettoye = ''.join(char.lower() for char in texte if char.isalnum())

    # Fonction récursive pour vérifier le palindrome
    def verifier(s):
        if len(s) <= 1:  # Cas de base si chaîne vide ou un seul caractère
            return True
        if s[0] != s[-1]:
            return False
        return verifier(s[1:-1]) # Ex : si s = "radar", alors s[1:-1] = "ada".

    # appelle la fonction récursive sur la chaîne
    return verifier(texte_nettoye)

# Exemples de test
print(is_palindrome())

# ====== 2.3 ======

import os  # On importe le module os pour travailler avec les dossiers et fichiers

def list_file (path="."):  # "." signifie le dossier actuel
    # os.walk parcourt tous les dossiers et fichiers du dossier
    for root, dirs, files in os.walk(path):
        print(f"\nDossier : {root}")  # On affiche le dossier courant
        for dir_name in dirs:  # On parcourt tous les sous-dossiers
            print(f"  Dossier  {dir_name}")  # On affiche chaque sous-dossier
        for file_name in files:  # même principe pour les fichiers
            print(f"  Fichier {file_name}")

if __name__ == "__main__":
    list_file()  # On appelle la fonction sur le dossier actuel

# ====== 3.1 ======

import string

def fun_a(s: str, n: int) -> bool:
    return len(s) >= n

def fun_b(s: str, n: int) -> bool:
    specials = sum(1 for ch in s if not ch.isalnum())
    return specials >= n

def fun_c(s: str, n: int) -> bool:
    digits = sum(1 for ch in s if ch.isdigit())
    return digits >= n

print(fun_a("Hello!", 5))     # True (length is 6)
print(fun_b("Hello!", 1))     # True ('!' is special)
print(fun_c("H3ll0!", 2))     # True ('3' and '0')

# ====== 3.2 & 3.3 ======

def fun1(s: str, n: int) -> bool:
    return len(s) >= n

def fun2(s: str, n: int) -> bool:
    specials = sum(1 for ch in s if not ch.isalnum())
    return specials >= n

def fun3(s: str, n: int) -> bool:
    digits = sum(1 for ch in s if ch.isdigit())
    return digits >= n

# Fonction générique qui appelle la règle choisie
def passcheck(rule_function, n: int, password: str) -> bool:

    if not callable(rule_function):
        raise TypeError("le premier argument doit être une fonction")
    if not isinstance(n, int):
        raise TypeError("Le deuxième argument doit être un nombre")
    if not isinstance(password, str):
        raise TypeError("Le troisième argument doit être une chaine ")

    return bool(rule_function(password, n))

print(passcheck(fun1, 16, "mysecretpassword")) # longueur
print(passcheck(fun2, 3,  "mysecretpassword!!!")) # caractères spéciaux
print(passcheck(fun3, 1,  "myp4ssword")) # chiffres




