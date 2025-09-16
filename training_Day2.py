a = 1+1
b = 30+12
c = 777 + (-735)
d = 1+2+3+5+7+11+13
print(a, b, c, d)

e = 84-42
f = 0-(-42)
g = 2*21
h = (-6)*(-7)
i = 2+5*8
j = (3+(3*4-2*2)*3-2)*2-3
k = 84//5

print(e, f, g, h, i, j, k)

#Différence entre / et //
# / est une simple division qui donnera un résultat en décimal, si le chiffre n'est pas entier
# // est une division, mais qui retournera forcément un résultat entier

# Task 2.1

# Fonction qui calcule la somme des n premiers termes de la suite 1, 11, 111, ...
# et renvoie cette somme ainsi que ses puissances de 2 à 5
def somme_et_puissances(n):
    # Fonction qui crée le c-ième terme de la suite
    def creer_terme(c):
        # Exemple : c=3 → "111" → 111
        return int("1" * c)

    # Calculer la somme des n premiers termes
    somme_total = 0
    for c in range(1, n + 1):
        terme = creer_terme(c)  # créer le c-ième terme
        somme_total += terme  # l'ajouter à la somme totale

    # Calculer les puissances de 2 à 5 de la somme
    puissance2 = somme_total ** 2
    puissance3 = somme_total ** 3
    puissance4 = somme_total ** 4
    puissance5 = somme_total ** 5

    # Retourner le résultat sous forme de dictionnaire
    return {
        "somme": somme_total,
        "puissance2": puissance2,
        "puissance3": puissance3,
        "puissance4": puissance4,
        "puissance5": puissance5
    }


# Exemple d'utilisation pour 3 termes
resultat = somme_et_puissances(3)  # 1 + 11 + 111
print(resultat)

#2.2
#La façon la plus simple de réaliser ce calcul avec le moins de caractère possible
print(17**1024)

#3.1
numerator = 42
denominator = 4

quotient = numerator // denominator
remainder = numerator % denominator
result = numerator / denominator

print(result)     # 10.5
print(quotient)   # 10
print(remainder)  # 2

#3.2
def is_odd(number):
    # Définition d'une fonction 'is_odd' qui prend un argument 'number'.
    # Cette fonction va vérifier si le nombre donné est impair.

    return number % 2 != 0
    # Retourne True si le reste de la division de 'number' par 2 n'est pas zéro,
    # ce qui signifie que le nombre est impair. Sinon, retourne False.

#Test
num = 6
if is_odd(num):
    print(f"{num} is odd")
else:
    print(f"{num} is even")

#3.3
def somme_chiffres(n):
    return sum(int(digit) for digit in str(n))
    #convertit le nombre n en texte, parcourt chacun de ses chiffres, les transforme en entiers puis en fait la somme totale

# Tests
nums = [123434565, 345567426, 44490320097]

for number in nums:
    print(f"Somme des chiffres de {number} = {somme_chiffres(number)}")

#3.4
def partie_entiere(x):
    # On enlève la partie décimal pour garder uniquement la partie entière
    return int(x)

# Tests
nums = [12.24, 424242.8412]

for number in nums:
    print(f"Partie décimale de {number} = {partie_entiere(number)}")


#3.5
def partie_decimale(x):
    # On enlève la partie entière pour garder uniquement la partie décimale
    return x - int(x)

# Tests
nums = [12.24, 424242.8412]

for number in nums:
    print(f"Partie décimale de {number} = {partie_decimale(number)}")

#4.1
result = 0

for i in range(1001):
    result += ((-1)**i) / (2 * i + 1)

result *= 4

print(round(result,6))








