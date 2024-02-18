import random
from itertools import permutations

"""Each agency has a name (a string) and each candidate has a name (a string).
The same number n of agencies and candidates. 
An instance is:
    + A dictionary containing the choices of the agencies: 
    its keys are the names of agencies and the value of an entry 
    is the list of choices of this agency. 
    + A dictionary containing the choices of the candidates: 
    its keys are the names of candidates and the value of an entry 
    is the list of choices of this candidate.
Each list must be a permutation of the n elements of the choices.

An assignment is: 
    a candidate C for each agency A and 
    an agency A for each candidate C.
    This must be symmetric: A->C iff C->A.
An assignment is represented by two dictionaries. Each element (candidate or 
agency) is a key and its assigned element is a value. 
"""

#------------------------------------------------------------------------------
def extract_instance_from_file(file):
    """Get the instance in the file. Return n + a dictionary containing the
    choices of the n agencies + a dictionary containing the choices of the
    n candidates (return a 3-tuple).
    The format of a file is:
    n (alone on the first line)
    followed by n lists for agencies followed by n lists for candidates.
    Each line is X:Y1:Y2:...:Yn where X is agency or candidate and the Yi's are
    the choices of X. The separator is ':' with no space between elements."""
    with open(file, "r", encoding="utf8") as f:
        agen = {}
        cand = {}
        c = 0
        for l in f:
            x = l.strip("\n").split(":")
            if (len(x) == 1):
                t = int(x[0])
            else:
                key = x[0]
                value = []
                for i in range(1, t+1):
                    value.append(x[i])

                if (c < t):
                    if key not in agen.keys():
                        agen[key] = value
                    else:
                        agen[key].append(value)
                    c += 1
                else:
                    if key not in cand.keys():
                        cand[key] = value
                    else:
                        cand[key].append(value)
        return t, agen, cand

print(extract_instance_from_file("affect.txt"))

#------------------------------------------------------------------------------
def is_coherent(choices_agencies, choices_candidates):
    """Function that verifies if the two dictionaries are coherent i.e. if
     each value is a list containing each appropriated element exactly once.
      Returns True if it is the case and raises an
      Exception('Incorrect choices') otherwise."""
    pass


#------------------------------------------------------------------------------
def generate_random_instance(n, version_number=1):
    """Generate a random instance with n agencies, n candidates and put the
    result in a file that is named GSEntries_Rand_{n}_{version_number}
    (for example GSEntries_Rand_10_3) to distinguish different random files."""
    pass


#------------------------------------------------------------------------------
def is_assignment_symmetric(agen_assignment, candidate_assignment):
    """Boolean function that returns True if the assignments are coherent,
    symmetric."""
    pass

#------------------------------------------------------------------------------
factorielle = lambda n: n * factorielle(n-1) if n != 0 else 1
def number_of_non_stable_couples(agencies_assign, candidates_assign,
                                 agencies_choices, candidates_choices):
    """Returns the number of non stable couples in the assignment."""

    """c = list(agencies_assign.keys())
    a = list(candidates_choices.keys())
    valid_pairings = [sorted(zip(i, a)) for i in permutations(c)]
    return factorielle(len(agencies_assign)) - len(valid_pairings)"""

    nbr=0
    for i in agencies_assign:
        for j in candidates_assign:
            if(candidates_assign[j].index(i) < candidates_assign[j].index(candidates_choices[j])):
                if(agencies_assign[i].index(j) < agencies_assign[i].index(agencies_choices[i])):
                    nbr+=1
    return nbr

#------------------------------------------------------------------------------
def generate_random_assignment(agencies_choices, candidates_choices):
    """Returns a random assignment as a 2 tuple of dictionaries."""
    liste = list(candidates_choices.keys())
    random.shuffle(liste)
    agenceChoix = {a:c for a,c in zip(agencies_choices.keys(), liste)}
    candidatChoix = {c:a for a,c in agenceChoix.items()}
    return agenceChoix, candidatChoix

#------------------------------------------------------------------------------
def comptes_assignements(agencies_assignement,agencies_choices):
    l = []
    for key in agencies_choices.keys():
        if agencies_assignement.get(key) == None or agencies_assignement[key] == "None":
            l.append(key)
    return l

def test_dico(dico,correspondance):
    return dico.get(correspondance) == None or dico[correspondance] == "None"

def Algo(agencies_choices, candidates_choices):
    agencies_assignement = {}
    candidates_assignement = {}
    agences_non_assignees = comptes_assignements(agencies_assignement,agencies_choices)

    while(len(agences_non_assignees) > 0):
        agence_act = agences_non_assignees[0]
        l_agence_act = agencies_choices[agence_act]
        candidat_act_i = 0
        while(test_dico(agencies_assignement, agence_act)):
            candidat_act = l_agence_act[candidat_act_i]
            if test_dico(candidates_assignement, candidat_act):
                agencies_assignement[agence_act] = candidat_act
                candidates_assignement[candidat_act] = agence_act
            elif candidates_choices[candidat_act].index(agence_act) < candidates_choices[candidat_act].index(candidates_assignement[candidat_act]):
                agencies_assignement[candidates_assignement[candidat_act]] = "None"
                agencies_assignement[agence_act] = candidat_act
                candidates_assignement[candidat_act] = agence_act
            candidat_act_i += 1
        agences_non_assignees = comptes_assignements(agencies_assignement,agencies_choices)

    return (agencies_assignement,candidates_assignement)

#------------------------------------------------------------------------------
def generate_random_instance(n, version_number=1):
    """Generate a random instance with n agencies, n candidates and put the
    result in a file that is named GSEntries_Rand_{n}_{version_number}
    (for example GSEntries_Rand_10_3) to distinguish different random files."""
    file = f"GSEntries_Rand_{n}_{version_number}.txt"
    name_liste = ["A","C"]
    with open(file, "w", encoding="utf8") as f:
       f.write(f"{n}\n")
       for name in range(len(name_liste)):
            for qqc in range(1,n+1):
                choix = list(range(1,n+1))
                f.write(f"{name_liste[name]}{qqc}:")
                for i in range(n):
                    C = random.choice(choix)
                    del choix[choix.index(C)]
                    f.write(f"{name_liste[len(name_liste)-1-name]}{C}")
                    if i == n-1:
                        f.write("\n")
                    else:
                        f.write(":")


print("------------------------------")
(a,b,c) = extract_instance_from_file("affect.txt")
(d,e) = generate_random_assignment(b,c)
print(b,c)
print("------------------------------")
print(Algo(b,c))
