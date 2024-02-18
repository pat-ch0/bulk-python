import time
import math
from math import sqrt

# Dans cette activité, tous les entiers sont positifs.
# Soit n un entier.
# On dit que d est un "diviseur strict" de n si d divise n et d<n.
# On dira que deux entiers n et m sont "couplés" si :
# la somme des diviseurs stricts de n est égale à m et la somme des
# diviseurs stricts de m est égale à n.
# NB : n et m peuvent avoir la même valeur (un entier peut donc
# être couplé avec lui même).

# Ecrivez la fonction Booléenne qui prend en entrée deux entiers et
# retourne la valeur Booléenne vrai si ces deux entiers sont couplés.

def sum_divisors(n):
    sum = 0
    if (n%2 == 0):
        for i in range(1, n//2 + 1):
            if (n%i == 0):
                sum += i
    else:
        for i in range(1, n//3 + 1):
            if (n%i == 0):
                sum += i
    return sum

def sont_couplés(n, m):
    return (sum_divisors(n) == m and sum_divisors(m) == n)

print(sont_couplés(9, 88))
print(sont_couplés(7, 7))

# Ecrivez la fonction qui prend en entrée un entier n_max et affiche toutes
# les paires n, m d'entiers couplés pour tout n < n_max.
# Chaque paire ne doit être affichée qu'une seule fois.

def affiche_tous_couplés(n_max):
    for n in range(1, n_max):
        m = sum_divisors(n)
        if n <= m and sum_divisors(m)==n:
            print(f"{n}, {m}")

begin = time.time()
affiche_tous_couplés(1_000)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)

begin = time.time()
affiche_tous_couplés(10_000)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)

begin = time.time()
affiche_tous_couplés(500_000)
print(f"Duration = {time.time() - begin} seconds to complete.")
print("-"*50)