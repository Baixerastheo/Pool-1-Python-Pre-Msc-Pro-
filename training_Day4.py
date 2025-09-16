# ====== 1.1 ======
#(42 > 12) true
#(12 = 12) false
#(12 == 12) true
#(”hello” == ”world”) false
#(218 >= 118) true
#(”a”.upper() == ”A”) true
#(1 ∗ 2 ∗ 3 ∗ 4 <= 9) false
#(”z” in ”azerty”) true

# ====== 1.2 ======

number = int(input("Enter an integer: "))

if number == 42:
    print("This is correct!")

# ====== 1.3 ======

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("this is even number!")
else:
    print("this is odd number!")

# ====== 1.4 ======

user_string = input("Enter the access code: ")

if user_string == "open sesame":
    print("access granted")
elif user_string == "will you open, you goddamn !@&/°":
    print("access fucking granted")
else:
    print("access denied")

# ====== 1.5 ======

user_int = int(input("Enter an integer: "))

match user_int:
    case 42:
        print("a")
    case 21:
        print("b")
    case int() as number if number % 2 == 0:
        print("c")
    case int() as number if number / 2 < 21:
        print("d")
    case int() as number if number % 2 != 0 and number >= 45:
        print("e")
    case _:
        print("f")

# ====== 1.6 ======

a = 42
b = 41

if a == b:
    print("A and B are the same")

if b <= a:
    print("B is equal to or less than A")

if b != a:
    print("B is different from A")

# ====== 2.1 ======

[print(num) for num in range(1,1001)]

# ====== 2.2 ======

user_char = input("Enter a string: ")

for char in user_char:
    print(char * 2, end="")
print()

# ====== 2.3 ======

[print(number) for number in range(9996, 0, -7)]

# ====== 2.4 ======

for integer in range(-30, 31):
    match integer:
        case int() as num if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        case int() as num if num % 3 == 0:
            print("Fizz")
        case int() as num if num % 5 == 0:
            print("Buzz")
        case _:
            print(integer)

# ====== 2.5 ======

def bottle_text(n):
    return f"{n} bottle{'s' if n > 1 else ''} of beer on the wall"

for bottle in range(99, 0, -1):
        print(f"{bottle_text(bottle)} ")
        print(f"{bottle} If one of the bottles just happen to fall, ")
        print(f"{bottle_text(bottle-1)}")

# ====== 2.6 ======
n = int(input("Enter an integer: "))

for i in range(2, n//2+1):
    multiples = []
    for j in range(n-1, 0, -1):
        if j % i == 0:
            multiples.append(j)
    print(multiples)

# ====== Challenges ======

while 1:
    n,s=input("n str: ").split(maxsplit=1);n=int(n)
    if n==0:break
    print(n if any(v in s for v in"aeiouAEIOU")or n>=42 else s)

# ====== 3.1 ======

msg = input("Message à chiffrer : ")
key = int(input("Clé (1-25) : ")) % 26   # le % 26 évite les erreurs si on tape >25

res = ""
for c in msg:
    if c.isalpha():                        # lettre ?
        base = 'A' if c.isupper() else 'a'  # point de départ selon maj/min
        res += chr((ord(c) - ord(base) + key) % 26 + ord(base))
    else:
        res += c                            # laisse espaces et ponctuation
print("Chiffré :", res)

# ====== 3.2 ======

def decrypt_all(cipher):
    for key in range(1, 26):
        plain = ""
        for ch in cipher:
            if ch.isalpha():
                base = 'A' if ch.isupper() else 'a'
                # pour décrypter, on soustrait la clé
                plain += chr((ord(ch) - ord(base) - key) % 26 + ord(base))
            else:
                plain += ch
        print(f"Clé {key:2d} : {plain}")

# Exemple d'utilisation
texte = input("Texte chiffré (Caesar) : ")
decrypt_all(texte)

# ====== 3.3 ======

def vigenere(txt, key, decrypt=False):
    key = key.lower()
    klen = len(key) # key length
    out = []
    for i, ch in enumerate(txt):
        if ch.isalpha():
            base = 'A' if ch.isupper() else 'a'
            shift = ord(key[i % klen]) - ord('a')
            if decrypt: shift = -shift
            out.append(chr((ord(ch) - ord(base) + shift) % 26 + ord(base)))
        else:
            out.append(ch)
    return ''.join(out)

# Ex :
msg = input("Texte : ")
k   = input("Clé  : ")

print("Chiffré  :", vigenere(msg, k))            # encryption
print("Déchiffré:", vigenere(msg, k, True))      # decryption






