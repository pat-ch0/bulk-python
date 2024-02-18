print("-"*14 + "\n Les exceptions \n" + "-"*14)

# En général, une exception est levée lorsque l'exécution du programme
# rencontre un problème. Par exemple, évaluer 1/0 provoque :
# ZeroDivisionError: division by zero 
# Par défaut (si rien n'est prévu pour la contrôler) l'arrivée d'une exception
# termine l'exécution du programme (erreur).
# Il est possible de provoquer (volontairement) des exceptions. Plusieurs
# manières sont possibles. La plus simple (limitée) est d'utiliser :

# raise(Exception("Mon exception à moi"))

# qui va provoquer :
# Exception: Mon exception à moi

# Pour aller plus loin et contrôler ses exceptions.

class PasDeChance(Exception): # Déf. d'une exception (hérite de Exception).
    pass

import random

def exception_random():
    """Fonction qui tire de manière aléatoire True ou False et retourne soit
    la chaine 'Youpi' (si True) soit lève une exception PasDeChance. """
    choix = random.choice([True, False])
    if choix:
        return "Youpi !"
    else:
        raise(PasDeChance)

# exception_random() va donc soit retourner quelque chose, soit provoquer une
# exception particulière "définie" un peu plus haut (cette fonction n'a aucun
# intérêt...).

# Il est possible de contrôler les exceptions pour éviter une terminaison
# en erreur avec try: ... except

def g():
    print("Les instructions AVANT le try.")
    try:
        print(f"J'ai eu de la chance {exception_random()}") 
    except PasDeChance: # Ce qu'il faut faire si cette exception est levée :
        print("Grr, pas de chance...")
    print("Les instructions APRES le try")

g()
g()
g()


print("-"*30 + "\n Les itérateurs (introduction) \n" + "-"*30)

# Une liste, un set ou un dictionnaire sont des objets itérables.
# Il est donc possible d'accéder à leurs éléments avec une boucle for.
# Mais il est possible d'y accéder aussi avec la fonction next(it) où it est
# un itérateur sur l'objet.

# Pour créer un itérateur à partir d'un objet itérable X, utiliser : iter(X) 

l = list(range(5)) # Création d'une liste l, objet itérable.
it = iter(l)  # Création d'un itérateur à partir d'un objet itérable.

print(f"La liste l est {l} et it est un itérateur sur l : {it}")
# it est maintenant un itérateur qui peut être utilisé pour progresser dans
# la liste grâce à next(it) qui va donner le prochain élément à chaque appel.

x = next(it)
print(f"Le 1er élément de l'itérateur it 'capturé' avec next(it) est {x}")
x = next(it)
print(f"Le 2ème élément de l'itérateur it 'capturé' avec next(it) est {x}")
print(f"etc... La liste d'origine a {len(l)} éléments.")
print(f"Il est alors possible d'utiliser l'itérateur it {len(l)} fois en tout.")
print("Au delà, l'exception spécifique StopIteration est produite et" +
      " l'itérateur est 'consommé'.")
print("Il ne peut alors plus être utilisé (mais la liste n'est pas affectée)")

# Remarque : en général next(...) n'est pas utilisé pour des listes ou des sets.
# Il est possible d'itérer facilement sur leurs éléments sans utiliser next()
# et sans risquer l'arrivée d'une désagréable exception StopIteration lorsque
# l'on itère trop. 

# Mais un fichier (voir plus loin) est itérable et il est parfois utile de le
# parcourir ainsi, en itérant sur ses lignes.

# Il est possible de créer des itérateurs avec autre chose que iter(X)

# Nous verrons plus tard des fonctions qui sont des itérateurs. Pour l'instant,
# faisons un détour par ce que l'on va appeler des 'itérateurs expressions'. 

# Voici un exemple : 
it = (x**2 for x in range(6)) # Ceci est un itérateur, pas un tuple.

# Notez les (...) pour le construire. it est maintenant un itérateur qui ne
# produit rien tant qu'il n'est pas sollicité/utilisé (avec next(it) ou une
# boucle for). Les diverses valeurs peuvent être obtenues avec next(it),
# l'une après l'autre. Avantage : utiliser ces valeurs sans avoir à les pré-
# calculer et à les stocker. Accès à la suivante au moment où on en a besoin...
# Un itérateur prend peu de place mémoire. 


print("-"*14 + "\n Les fichiers \n" + "-"*14)

# Pour créer un nouveau fichier et écrire des choses à l'intérieur il est
# intéressant d'utiliser un gestionnaire de contexte (context manager) qui
# évite d'avoir à faire explicitement l'opération de fermeture du fichier.
# Le fichier est fermé proprement, quoi qu'il se passe.

file = "FICHIER_ESSAI"  # Le nom du fichier dans une chaine.

# Pour ouvrir un fichier, utiliser open(...) en spécifiant :
#   Le nom du fichier,
#   "r" pour read (lire) ou "w" pour write (écrire),
#   Le codage utilisé pour lire ou écrire. Nous allons utiliser utf8.
# Le context manager s'exprime avec 'with ... as' où ce qui suit as est ici
# le nom qui va servir à utiliser le fichier.
# Le code python dans le block du with peut alors utiliser le fichier ouvert. 

# Pour écrire dans un fichier f, utiliser f.write(...).
# Exemple. Exécutez le code suivant et regardez le contenu du fichier produit.

with open(file, "w", encoding="utf8") as f:
    f.write("Le fichier des carrés.\n")
    for i in range(6):
        f.write(f"Le carré de {i} est {i**2} \n")
    f.write("Fin du fichier.")

# Pour lire dans un fichier dont l'itérateur est f, voici plusieurs manières
# de procéder.
# La première utilise next(f) pour passer de ligne en ligne, jusqu'à la fin de
# consommation de l'itérateur et la levée de l'exception StopIteration.

# En faisant comme suit, les lignes seront affichées mais l'exécution va se
# terminer sur l'exception StopIteration.

##with open(file, "r", encoding="utf8") as f:
##    while True:
##        ligne = next(f)
##        print(ligne)

# Sinon, il est possible d'itérer avec une boucle for par exemple.

print(f"Le contenu du fichier {file} est :")
with open(file, "r", encoding="utf8") as f:
    for l in f:
        print(l)

# Ici la variable l "prend" les lignes successives du fichier.
# Notez que comme elles sont imprimées avec print( ) on passe à la ligne après
# chaque print() (effet du print) ET on affiche aussi le saut de ligne à
# la fin de chaque ligne du fichier (ce qui provoque un autre saut de ligne).

# Pour éviter ces sauts de lignes on peut faire par exemple :

print(f"Le contenu du fichier {file} (sans sauts de lignes inutiles) est :")
with open(file, "r", encoding="utf8") as f:
    for l in f:
        print(l, end = "")