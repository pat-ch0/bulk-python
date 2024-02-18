"""Codage de Huffman.
Cette version est purement pédagogique et ne pourrait pas servir de mise en
production efficace.
Chaque étape donne lieu à des objets intermédiares qui peuvent être affichés,
visualisés, contrôlés.
Cette version code des fichiers en UTF8 dont certains caractères sont codés sur
un, deux, trois ou quatre octets."""


def construit_liste_ss_arbres_caracteres_nombres(fichier, affiche = True):
    """Pour chaque caractère c du fichier, construit une liste :
    [(c,n), None, None] où n est le nombre de fois que c est présent dans le
    fichier. Une telle liste sera vue plus tard comme une feuille.
    Si affiche == True, afficher les paires (c,n) dans l'ordre croissant de n.
    """
    L = []
    dico = {}
    with open(fichier, "r", encoding="utf-8") as f:
        for line in f:
            for c in line:
                if c in dico:
                    dico[c] += 1
                else:
                    dico[c] = 1

    for i in dico.keys():
        l = []
        l.append((i, dico[i]))
        l.append(None)
        l.append(None)
        L.append(l)
        
    L.sort(key = lambda tup: tup[0][1])

    if affiche:
        print(L)
    return L


def construit_arbre_huffman_depuis_liste(liste_car_nbre):
    """À partir de la liste composée de listes du type [(c,n), None, None],
    construit et retourne l'arbre de Huffman suivant l'algorithme classique.
    Le résultat (l'arbre) est une liste composée de listes du type :
    [(c,n), a_1, a_2] avec :
    + n un entier.
    + c un caractère ; dans un cas a_1 et a_2 sont None et c'est une feuille
        ou c est None ; dans l'autre cas c'est un noeud interne et a_1 et a_2 sont
        des sous-arbres. Par convention, a_1 est le sous-arbre gauche codant 0
        et a_1 le sous-arbre droit codant 1."""
    arbre = liste_car_nbre
    while len(arbre) > 1:
        # Retirer les 2 noeuds ayant les plus petites valeurs n
        a_1 = min(arbre, key=lambda noeud: noeud[0][1])
        arbre.remove(a_1)
        a_2 = min(arbre, key=lambda noeud: noeud[0][1])
        arbre.remove(a_2)
        # a_1 et a_2 deviennent sous-arbres d'un nouveau noeud, somme des 2
        a_nouveau = (None, a_1[0][1] + a_2[0][1])
        arbre.append([a_nouveau, a_1, a_2])
    return arbre[0]


def construit_table_codage_depuis_arbre_huffman(arbre):
    """Construit la table de codage à partir de l'arbre de Huffman.
    Le resultat est un dictionnaire dont les clés sont les caractères et les
    valeurs sont les codes binaires correspondant issus de l'arbre. Un code
    binaire est retourné ici sous forme de chaine de cararctères de '0' et '1'.
    """
    def iter_rec_chaines_binaires(arbre, chaine_courante):
        if arbre[1] == None and arbre[2] == None: # feuille
            yield arbre[0][0], chaine_courante
        else:
            yield from iter_rec_chaines_binaires(arbre[1], chaine_courante + "0")
            yield from iter_rec_chaines_binaires(arbre[2], chaine_courante + "1")

    table = {}
    it = iter_rec_chaines_binaires(arbre, "")
    for (car, chaine) in it:
        table[car] = chaine
    return table


def code_fichier(fichier, table_codage):
    """Code chaque caractère du fichier avec la table de codage dont les clés
    sont les caractères et les valeurs les codes binaires sous forme de chaines
    de '0' et de '1'.
    Le résultat est une chaine de caractères de '0' et de '1'."""
    result = ""
    with open(fichier, "r", encoding="utf8") as f:
        for ligne in f:
            result += "".join([table_codage[car] for car in ligne])
    return result


def decode_message(message_binaire, arbre):
    """Prend en entrée une chaine de caractères de '0' et de '1' (message codé)
    + un arbre de huffman. Retourne le décodage sous forme d'une chaine de
    caractères."""
    result = ""
    sous_arbre = arbre
    for x in message_binaire:
        if x == '0':
            sous_arbre = sous_arbre[1]
            if sous_arbre[1] == None and sous_arbre[2] == None:
                result += sous_arbre[0][0]
                sous_arbre = arbre
        elif x == '1':
            sous_arbre = sous_arbre[2]
            if sous_arbre[1] == None and sous_arbre[2] == None:
                result += sous_arbre[0][0]
                sous_arbre = arbre
    return result


#----- Manipulations de ces fonctions.

# Partie codage du fichier : 
fichier = "Essai_Huffman.txt"
#fichier = "Codage_Huffman_Simple.py" # Pour coder le fichier source...
liste_feuilles = construit_liste_ss_arbres_caracteres_nombres(fichier, False)
arbre = construit_arbre_huffman_depuis_liste(liste_feuilles)
table = construit_table_codage_depuis_arbre_huffman(arbre)
message_codé = code_fichier(fichier, table) # Codage Huffman en bin. du fichier

print(f"Le message codé est :\n{message_codé}")
print(10*"---")
print(f"La taille du message codé est de : {len(message_codé)} bits, soit " +
      f"{len(message_codé)/8} octets.")
print(10*"---")

# Partie décodage :
message_décodé = decode_message(message_codé, arbre)
print(f"Le message décodé est : \n{message_décodé}")
