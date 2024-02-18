def iter_syracuse(n):
    """Prend en entrée un entier n>0. Retourne un itérateur sur les éléments de
    la suite de syracuse lorsque le terme initial est n."""
    yield n
    while (n>1):
        n = n//2 if (n%2 == 0) else 3*n + 1
        yield n

it = iter_syracuse(8)
for x in it:
    print(f"{x}", end=" ")
print()

#------------------------------------------------------------------------------
def iter_fibo():
    """Générateur des éléments de la suite de Fibonacci."""
    fibUn = 0
    fibDeux = 1
    yield fibUn
    yield fibDeux
    while(1):
        fibUn, fibDeux = fibDeux, fibUn + fibDeux
        yield fibDeux

it = iter_fibo()
for x in range(10):
    print(next(it), end=" ")
print()

#------------------------------------------------------------------------------
def look_and_say_iter(z, k):
    """La suite Look and say mise en oeuvre avec un itérateur."""
    nex = []
    current = z[0]
    c = 0
    for i in range(k):
        for chiffre in z:
            if chiffre == current:
                c += 1
            else:
                nex.append(str(c))
                nex.append(current)
                current = chiffre
                c = 1
        nex.append(str(c))
        nex.append(current)
        yield " ".join(nex)
        z = "".join(nex)
        nex = []
        current = z[0]
        c = 0

suite = look_and_say_iter("1", 4)
for x in suite:
    print(f"{x}")

#------------------------------------------------------------------------------
def iter_tous_les_facteurs(mot):
    """Création d'un itérateur qui génère tous les facteurs non vides du mot
    donné en paramètre. Exemple : tous les facteurs de la chaine "abcd" sont :
    a ab abc abcd b bc bcd c cd d """
    for i in range(len(mot)):
        for j in range(i, len(mot)):
            yield mot[i : j+1]

it = iter_tous_les_facteurs("abcd")
for x in it:
    print(f"{x}")

#------------------------------------------------------------------------------
def iter_toutes_les_listes_binaires(n):
    """Itérateur produisant toutes les listes de {0, 1} de taille n."""
    for i in range(2**n):
        yield [int(i) for i in f"{i:0{n}b}"]

#------------------------------------------------------------------------------
def iter_nombres_premiers(v):
    """Itérateur produisant tous les nombres premiers à partir de v."""
    import math  # Bibliothèque autorisée si besoin.
    def premier(n):
        for x in range(2, int(math.sqrt(n)) + 1):
            if (n%x == 0):
                return False
            return True
    
    n = v if v>1 else 2
    while(1):
        if premier(n):
            yield n
        n += 1

#------------------------------------------------------------------------------
def iter_tous_les_sous_ensembles(ensemble):
    """Itérateur produisant tous les sous-ensembles possibles de l'ensemble
    donné en entrée."""
    l = [x for x in ensemble]
    n = len(l)
    it = iter_toutes_les_listes_binaires(n)
    for e in it:
        s = set()
        for i in range(n):
            if (e[i] == 1):
                s.add(l[i])
        yield s