#1.1
sentence = "I am the very long sentence intro a variable"
print(sentence)

#1.2
print(sentence[0])
print(sentence[16])

#1.3
print(sentence[0], sentence[5])

#2.1
all_caps = "A LOWER SENTENCE !!!!"
print(all_caps.lower())

#2.2
tututu_to_tatata = "tu tu tu"
print(tututu_to_tatata.replace("tu", "ta"))

#2.3
string = " Hello world !" #variable string
position = string.find ("a") #Cette méthode permet de trouver la position d'un caractère,
                            # en l'occurence le a n'existe pas dans cette phrase, donc il retournera -1
print ( position )

#2.4
p = "abcdefghij"
print (p [:: -2][:5][:: -1][3:])

print (p [:: -2]) #prend un caractère sur deux en partant de la fin
print (p [:5]) #prend les 5 premiers caractères
print (p [:: -1]) #prend tous les caractères en partant de la fin
print (p [3:]) #prend tous les caractères après le troisième

#2.5
#en sachant ce que donne chaque étape,
# [:: -2] donne jhfdb
# [:5] jhfdb, rien n'a changer vu que l'on prend les 5 premiers caractères
# [:: -1] dbfhj, tous les caractères à l'envers
# [3:] hj, tous les caractères après les 3 premiers

#Donc la formule simplifiée serait
print(p[7::2]) #on prend 2 caractères après 7 caractères donc hj

#2.6
stringRepeat = " I am the string repeat 10 times"
print (stringRepeat * 10)

#2.7
#print("hello" + 42) je suppose que ce code avait pour but de répeter le hello 42 fois
print("hello\n"* 42) #il suffit de remplacer l'addition par une multiplication, le \n permet de sauter des lignes

#2.8
s1, s2, s3 = "42", "is", " the answer "
# le join concatène les éléments entre eux et le .strip permet d'enlever les deux espaces de début et de fin de s3
print(" ".join([s1, s2, s3.strip()]))

#3.1
Username = input("Saisir votre nom : ")

#méthode permettant de mettre la première lettre en majuscule
formatted_username = (Username.capitalize())

print(f"Bonjour, {formatted_username}!")

#3.2
user_var = input("Saisir quelque chose : ")
print(type(user_var))

user_var = int(input("Saisir quelque chose : "))
print(type(user_var))

#3.3

a = int(input("Saisir un nombre : "))
b = int(input("Saisir un nombre : "))
print(f"La somme des deux nombres est {a + b}")

#3.4
user_str = input("Saisir une phrase")
result = ""
liste_mot = user_str.split()
for i in liste_mot:
    result += i[0]
print(result)

#3.5

LANGUAGE_PROFILES = {
    "english": {
        "e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0, "n": 6.7, "s": 6.3, "h": 6.1, "r": 6.0, "d": 4.3, "l": 4.0, "c": 2.8, "u": 2.8, "m": 2.4, "w": 2.4, "f": 2.2, "g": 2.0, "y": 2.0, "p": 1.9, "b": 1.5, "v": 1.0, "k": 0.8, "j": 0.2, "x": 0.2, "q": 0.1, "z": 0.1
    },
    "french": {
        "e": 14.7, "a": 7.6, "i": 7.5, "s": 7.9, "n": 7.2, "r": 6.6, "t": 7.0, "o": 5.8, "l": 5.5, "u": 6.3, "d": 3.7, "c": 3.3, "m": 2.7, "p": 3.0, "v": 1.8, "q": 1.4, "f": 1.1, "b": 0.9, "g": 1.0, "h": 1.1, "j": 0.3, "x": 0.4, "y": 0.3, "z": 0.1, "é": 1.5, "è": 0.8, "ê": 0.6, "ë": 0.1, "à": 0.5, "ù": 0.1, "ç": 0.3
    },
    "spanish": {
        "e": 13.7, "a": 12.5, "o": 8.7, "s": 7.9, "n": 7.0, "r": 6.9, "l": 5.2, "d": 5.0, "c": 4.7, "t": 4.6, "u": 3.9, "m": 3.2, "p": 2.5, "b": 1.4, "g": 1.0, "v": 0.9, "y": 1.0, "q": 1.0, "h": 0.7, "f": 0.5, "z": 0.4, "j": 0.5, "ñ": 0.3, "á": 0.4, "é": 0.4, "í": 0.4, "ó": 0.4, "ú": 0.4
    },
    "portuguese": {
        "a": 14.6, "e": 12.6, "o": 10.7, "s": 7.8, "r": 6.7, "i": 6.2, "n": 5.0, "d": 4.9, "m": 4.7, "u": 4.6, "t": 4.3, "c": 3.9, "l": 2.8, "p": 2.5, "v": 1.6, "g": 1.3, "h": 1.2, "q": 1.2, "b": 1.0, "f": 1.0, "z": 0.5, "j": 0.4, "x": 0.2, "á": 0.5, "â": 0.3, "ã": 0.5, "é": 0.4, "ê": 0.2, "í": 0.2, "ó": 0.4, "ô": 0.2, "õ": 0.3, "ú": 0.2, "ç": 0.3
    },
    "italian": {
        "e": 11.8, "a": 11.7, "i": 10.7, "o": 9.8, "n": 6.9, "l": 6.5, "r": 6.4, "t": 5.6, "s": 4.9, "c": 4.5, "d": 3.7, "u": 3.2, "m": 2.9, "p": 3.0, "v": 2.1, "g": 1.6, "h": 0.6, "b": 1.0, "f": 1.1, "z": 1.0, "à": 0.2, "è": 0.2, "é": 0.2, "ì": 0.2, "ò": 0.2, "ù": 0.2
    },
    "german": {
        "e": 17.4, "n": 9.8, "i": 7.6, "s": 7.3, "r": 7.0, "a": 6.5, "t": 6.2, "d": 5.1, "h": 4.8, "u": 4.3, "l": 3.4, "c": 3.1, "g": 3.0, "m": 2.5, "o": 2.5, "b": 1.9, "w": 1.9, "f": 1.7, "k": 1.2, "z": 1.1, "ä": 0.6, "ö": 0.4, "ü": 0.7, "ß": 0.3, "j": 0.3, "v": 0.8
    },
# deuxième partie, trop longue pour tenir en un seul post
    "dutch": {
        "e": 18.9, "n": 10.0, "a": 7.5, "t": 6.8, "i": 6.5, "r": 6.4, "o": 6.1, "d": 5.6, "s": 3.7, "l": 3.6, "g": 3.4, "v": 2.8, "h": 2.4, "k": 2.3, "m": 2.2, "u": 1.9, "b": 1.6, "p": 1.6, "w": 1.5, "j": 1.5, "z": 1.4, "f": 0.8, "c": 0.6, "x": 0.1, "y": 0.1, "é": 0.2, "è": 0.1, "ë": 0.1
    },
    "swedish": {
        "e": 10.2, "a": 9.4, "n": 8.6, "t": 7.7, "r": 8.4, "s": 6.6, "l": 5.3, "d": 4.7, "o": 4.5, "i": 4.8, "m": 3.5, "g": 2.9, "k": 3.1, "v": 2.4, "h": 2.1, "u": 1.9, "f": 2.0, "b": 1.3, "p": 1.8, "å": 1.3, "ä": 1.8, "ö": 1.3, "y": 0.6, "j": 0.6
    },
    "polish": {
        "a": 8.9, "i": 8.2, "e": 7.7, "o": 7.6, "z": 6.2, "n": 5.5, "r": 4.7, "w": 4.7, "y": 4.0, "c": 3.9, "l": 3.7, "t": 3.3, "s": 3.2, "d": 2.5, "k": 2.5, "p": 2.4, "m": 2.4, "u": 2.4, "j": 2.3, "b": 1.5, "g": 1.5, "ę": 1.1, "ł": 2.1, "ś": 0.8, "ń": 0.8, "ć": 0.8, "ó": 0.7, "ź": 0.3, "ż": 0.4
    },
    "turkish": {
        "a": 12.9, "e": 8.6, "i": 8.3, "n": 7.9, "r": 6.7,"l": 6.0, "d": 5.2, "k": 4.7, "t": 3.6, "u": 3.2, "m": 3.0, "o": 2.9, "b": 2.8, "s": 2.7, "y": 2.7, "v": 2.4, "z": 1.5, "g": 1.3, "ç": 1.2, "ş": 1.2, "ğ": 1.1, "ı": 5.1, "ö": 0.8, "ü": 0.9, "c": 0.7, "h": 0.6, "f": 0.5, "j": 0.4, "p": 0.3
    },
    "esperanto": {
        "a": 12.0, "e": 8.9, "i": 10.0, "o": 9.8, "u": 9.4, "n": 8.5, "l": 6.1, "s": 5.7, "r": 5.6, "t": 4.8, "k": 4.5, "m": 3.7, "d": 3.5, "p": 3.1, "v": 2.1, "g": 2.0, "b": 1.8, "f": 1.4, "h": 1.2, "ĉ": 1.0, "ĝ": 0.8, "ĵ": 0.5, "ŝ": 0.6, "ŭ": 0.3, "ĥ": 0.2, "z": 0.3, "c": 0.3, "j": 0.6
    }
}

print("Enter a text :")
text = input()
text = text.lower()
occurence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reference = "abcdefghijklmnopqrstuvwxyz"
refpays = ["english","french","esperanto","turkish","polish","swedish","dutch","german","italian","portuguese","spanish"]

for i in range(26):
    occurence[i] = text.count(reference[i])

frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(26):
    frequency[i] = occurence[i] / len(text) * 100

score = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(11):
    for j in range(26):
        if reference[j] in LANGUAGE_PROFILES[refpays[i]] :
            score[i] += abs(frequency[j]-LANGUAGE_PROFILES[refpays[i]][reference[j]])

print("The language of this text is probably : " + refpays[score.index(min(score))])
