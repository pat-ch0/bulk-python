import random

"""Data structure of a formula F.
   -----------------------------
    A variable is a string (with no ',', no '&', no ' ' and no '-')
    A positive literal is a variable. 
    A negative literal is a variable with an additional '-' as first character.
    A clause is a list of literals.
    A formula is a list of clauses.
    
    The dictionary of a formula is the dictionary whose keys are the variables
    of the formula. 

   Boolean values of variables, literals, clauses, formulas.
   ---------------------------------------------------------
    An assignment for a formula is a Boolean value for each variable of the 
    dictionary of the formula. 
    Given a formula F and an assignment A:
        The boolean value of a positive literal with variable x is the Boolean
            value of A[x].
        The boolean value of a negative literal with variable x (-x) is the 
            Boolean value of not(A[x]).
        The boolean value of a clause is the logical OR Boolean value 
            of its literals. A clause is 'satisfied' if its value is True.
        The boolean value of a formula is the logical AND Boolean value 
            of its clauses. A formula is 'satisfied' if its value is True.
    
    Illustration.
    ------------
    F = [['a', '-b', 'c'], ['-a', 'b', '-d'], ['a', 'b', 'c'], ['-b', 'd', '-e']]
    The dictionary of F has keys 'a', 'b', 'c', 'd', 'e'
    An example of an assignment:
    {'a':False, 'b':True, 'c':True, 'd':False, 'e':False}
"""


def get_formula_from_file(file):
    """Extract a formula from file and returns it as a list.
    In file:
        A variable is a string (with no ',', no '&', no ' ' and no '-').
        A literal is either:
            a variable (positive literal) or a variable beginning with
            '-' (negative literal).
        Literals in clauses are separated by ','.
        Clauses are separated by '&'.
        Formula is on one line in the file.
    Example of formula: a,-b,cloclo&b,-a,-c&d,-a,-b&-cloclo,-name,-a,-b
    """
    final = []
    l = []
    with open(file, "r", encoding="utf8") as f:
        for ligne in f:
            l = ligne.split("&")
            for i in l:
                final.append(i.split(","))
    return final

def variable_of_literal(literal):
    """Returns the name of the variable of the literal."""
    if literal[0] == '-':
        return literal[1:len(literal)]
    else:
        return literal
    

def sign_of_literal(literal):
    """Returns the sign of the literal: '-' for a negative literal and
    '+' otherwise."""
    if literal[0] == '-':
        return '-'
    else:
        return '+'
    

def set_of_variables_from_formula(f):
    """Returns the set of the names of variables appearing in the formula."""
    var = set()
    for c in f:
        for literal in c:
            if not (variable_of_literal(literal) in var):
                var.add(variable_of_literal(literal))
    return var
    

def construct_dictionary_from_vars(set_of_vars):
    """Constructs a dictionary from the set of variables.
    The value of each entry is None (no assignment)."""
    dico ={}
    for var in set_of_vars:
        dico[var] = None
    return dico
    

def random_assignment(d):
    """Takes a dictionary as input and puts a random Boolean value to each
    variable. """
    boolist = [True,False]
    for literal in d.keys():
        d[literal] = random.choice(boolist)
    return d
    


def boolean_value_of_literal(assignment, literal):
    """Given an assignment and a literal, returns the Boolean value of the
       literal."""
    if literal[0] == '-':
        return not(assignment[variable_of_literal(literal)])
    else :
        return assignment[variable_of_literal(literal)]
    
    

def boolean_value_of_clause(assignment, clause):
    """Given an assignment and a clause, returns the Boolean value of the
       clause."""
    for literal in clause:
        if boolean_value_of_literal(assignment,literal):
            return True
    return False
    

def boolean_value_of_formula(assignment, formula):
    """Given an assignment and a formula, returns the Boolean value of the
       formula."""
    for clause in formula:
        if not(boolean_value_of_clause(assignment,clause)):
            return False
    return True
    

def number_of_true_clauses(assignment, formula):
    """Given an assignment and a formula, returns the number of clauses having
       a Boolean value True."""
    compteur = 0
    for clause in formula:
        if boolean_value_of_clause(assignment,clause):
            compteur += 1
    return compteur
    

def number_of_clauses(formula):
    """Returns the number of clauses of the formula."""
    return len(formula)
    

def pretty_print_formula(formula):
    """Print a nice/readable view of the formula."""
    for clause in range(len(formula)):
        s = ""
        for i in range(len(formula[clause])):
            s += formula[clause][i]
            if(formula[clause][i][0] != '-'):
                s += " "
            if (i < len(formula[clause])-1):
                s += " or "
        print("C" + str(clause) + " = " + s)


def pretty_print_assigned_formula(assignment, formula):
    """Print a nice/readable view of the formula with each variable replaced
       by its Boolean value; also print the value of each clause. Illustration
       True       not(False) True        = True
       not(True)  False      not(True)   = False
       True       False      True        = True"""
    for clause in formula:
        s = ""
        for literal in clause:
            if literal[0] == '-':
                s += "not(" + str(assignment[variable_of_literal(literal)]) + ")  "
            else:
                s += str(assignment[variable_of_literal(literal)]) + "       "
        print(s + "= " + str(boolean_value_of_clause(assignment,clause)))


def random_formula(n=26, c=10, min_len=1, max_len=10, file="FX"):
    """Generate a random formula with at most n variables, exactly c clauses,
       each with at least min_len literals and at most max_len literals.
    Put the final formula in file.
    Each variable must be a non capital letter (a, b, c,...,z). """
    boolist = ["","-"]
    formula = []
    for i in range(c):
        clause = []
        for j in range(random.randint(min_len,max_len)):
            clause.append(random.choice(boolist)+"x"+str(random.randint(1,n+1)))
        formula.append(",".join(clause))

    with open(file+".txt", "w", encoding="utf8") as f:
        f.write("&".join(formula))


def iter_toutes_les_listes_binaires(n):
    """Itérateur produisant toutes les listes de {0, 1} de taille n."""
    l = [0]*n
    yield l
    while l != [1]*n:
        pos = n-1
        verif = True
        while verif:
            if l[pos] == 0:
                l[pos] = 1
                verif = False
            else:
                l[pos] = 0
                pos = pos-1
        yield l

def iter_all_assignments(d):
    """An iterator to generate all the possible assignments of a dictionary d.
    NB: the call returns an iterator of assignments, not the assignments."""
    key = []
    for i in d.keys():
        key.append(i)
    it = iter_toutes_les_listes_binaires(len(key))
    for i in it:
        dico = {}
        for j in range(len(key)):
            if i[j] == 1:
                dico[key[j]] = True
            else:
                dico[key[j]] = False
        yield dico
    

def evaluate_all_assignments(formula):
    """Returns, for each possible assignment of the variables of the formula,
    the list of the number of satisfied clauses (with Boolean value True)."""
    l = []
    literalName = []
    for cause in formula:
        for literal in cause:
            literalName.append(variable_of_literal(literal))
    dico = construct_dictionary_from_vars(literalName)
    it = iter_all_assignments(dico)
    for i in it:
        l.append(number_of_true_clauses(i,formula))
    return l


"""
Example of pretty print of formula a,-b,c&-a,b,-d&a,b,c&-b,d,-e&a,-c,e :
 a or -b or  c
-a or  b or -d
 a or  b or  c
-b or  d or -e
 a or -c or  e

Example of a pretty print of an assignment for this formula:

False      not(False) False       = True
not(False) False      not(False)  = True
False      False      False       = False
not(False) False      not(True)   = True
False      not(False) True        = True """


"""Voici du code de test à ajouter après la définition de vos fonctions
(à la fin de votre fichier).
Interdiction de modifier les lignes suivantes. Interdition d'utiliser
une autre bibliothèque que random. Seuls les résultats des appels suivants
doivent s'afficher, rien d'autre. """

f1 = [['aa', '-bbbb', '-c'], ['-aa', '-bbbb', '-dd'], ['aa', 'bbbb', 'c'],
     ['-bbbb', 'd', '-e']]
dico_f1 = construct_dictionary_from_vars(set_of_variables_from_formula(f1))
print("La formule est :", f1)
print(f"L'ens. de ses var. est : {set_of_variables_from_formula(f1)}.")

print(f"La variable contenue dans le litéral {'aa'} est : " + 
      variable_of_literal('aa'))

print(f"La variable contenue dans le litéral {'-dd'} est : " +
      variable_of_literal("-dd"))

for var in dico_f1:
    dico_f1[var] = True

print("Voici une affectation où toutes les varaibles sont à True :\n",
      dico_f1)

print("Avec cette affectation on a les valeurs Boll. suivantes :")

une_clause = f1[0]
for litéral in une_clause:
      print(f"Le litéral {litéral} a la valeur : ",
            boolean_value_of_literal(dico_f1, litéral))

for clause in f1:
    print(f"La clause {clause} a la valeur : ",
        boolean_value_of_clause(dico_f1, clause))  

print(f"La formule a la valeur : ",
      boolean_value_of_formula(dico_f1, f1))

print(f"La formule a {number_of_true_clauses(dico_f1, f1)} clauses à Vrai.")

liste_nbr_clauses_vraies = evaluate_all_assignments(f1)
liste_nbr_clauses_vraies.sort()
print(f"Liste (triée) du nombre de clauses vraies de la formule : ")
print(liste_nbr_clauses_vraies)
print(f"La longueur de cette listes est : {len(liste_nbr_clauses_vraies)}.")

print("Construisons un itérateur d'affectations un peu plus gros...")
dico = {chr(i) : None for i in range(65, 65 + 26)} 
it = iter_all_assignments(dico)
print("Voici l'itérateur généré : ", it)
print("Explorons un peu cet itérateur...")
for _ in range(3):
    print(next(it))