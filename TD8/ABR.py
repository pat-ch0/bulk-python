"""Library to manipulate Binary search tree (named ABR here).
 An ABR is a list of 4 elements:
 [0] A left tree (an ABR),
 [1] A key: a tuple (value, label) where value must be numeric and
    label is any format.
 [2] A right tree (an ABR).
 [3] The parent (None if the node is the root of the ABR).
 Organisation of keys:
    + Keys of all nodes of left tree must have values strictly less than
    to the one of the node.
    + Keys of all nodes of right tree must have values greater than or equal
    to the one of the node.
    + An empty sub-tree (left or right) is referenced by a None value.
 Warning:
     + multiple keys having the same value are allowed here.
     + Multiple same keys are allowed here (this is not a set structure).
"""

def val_abr(abr):
    """Return the value of the ABR."""
    return abr[1][0]


def key_abr(abr):
    """Return the key of the ABR."""
    return abr[1]


def left_tree_abr(abr):
    """Return the left tree of the ABR."""
    return abr[0]


def right_tree_abr(abr):
    """Return the right tree of the ABR."""
    return abr[2]


def parent_abr(abr):
    """Return the parent tree of the ABR."""    
    return abr[3]


def create_abr(key, parent=None):
    """Create and return an ABR with given key and parent."""
    abr = [None, key, None, parent]
    return abr


def insert_abr(key, abr):
    """Insert Key=(value, label) in ABR. Warning: Does NOT verify if the key
    is already in ABR. Insertion in place (modification of the ABR)."""
    subabr = abr
    while(subabr[3] != None):
        if(subabr[1][0] > key[0]):
            subabr = subabr[0]
        else:
            subabr = subabr[2]
    abr = create_abr(key, subabr)


def find_minimum_key_abr(abr):
    """Find and return a key with minimum value of ABR.
    If several keys have minimum value, return one of them."""
    while(abr[0] != None):
        abr = abr[0]
    return abr[1]


def find_maximum_key_abr(abr):
    """Find and return a key with maximal value of ABR.
    If several keys have maximal value, return one of them."""
    while(abr[2] != None):
        abr = abr[2]
    return abr[1]


def find_abr(value, abr):
    """"Find and return a subtree of abr whose key have the value.
    If several keys have this value, return one of them and return None if
    the value is not present."""
    while(abr != None):
        if(abr[1][0] > value):
            abr = abr[0]
        else:
            abr = abr[2]
        if(abr == value):
            return abr
    return None


def find_minimum_subtree_abr(sub_abr):
    """Find and return a subtree whose root key has minimum value of ABR.
    If several keys have maximal value, return one of these trees."""
    pass


def list_of_keys_abr(abr):
    """Return the list of all the keys of ABR. Sorted in increasing values.
    """
    liste = []
    saveAbr = abr
    while(abr[0] != None):
        liste.append(abr[1])
        abr = abr[0]
    abr = saveAbr
    liste.append(abr[1])
    while(abr[2] != None):
        liste.append(abr[1])
        abr = abr[2]
    liste = liste.sort()
    return liste


def iter_on_keys_abr(abr):
    """An iterator on the keys of the ABR."""
    liste = list_of_keys_abr(abr)
    it = iter(liste)
    x = next(it)
    while(x != None):
        print(f"Key : {x}")
        x = next(it)


def len_abr(abr):
    """Return the number of keys in ABR. If several keys are the same, they are
    multiply counted."""
    return length(list_of_keys_abr(abr))


def print_abr(abr):
    """Print a "flat" (list) view of the ABR."""
    print(7 * "-")
    print(f"The root key of the ABR is {key_abr(abr)} and ABR is: \n{abr}")


def pretty_print_abr(abr, level=0):
    """Print a horizontal tree-like view of the ABR.
    Does NOT print parent field."""
    def dec(l):
        return (4 * l) * " "
    if left_tree_abr(abr) is not None:
        pretty_print_abr(left_tree_abr(abr), level + 1)
    else:
        print(dec(level + 1) + "Empty")
    print(dec(level) + f"{key_abr(abr)}")
    if right_tree_abr(abr) is not None:
        pretty_print_abr(right_tree_abr(abr), level + 1)
    else:
        print(dec(level + 1) + "Empty")


def error_structure_abr(message):
    print(f"ERROR: ABR not coherent. " + message)
    return False


def is_coherent_abr(abr):
    """Check is the ABR is well structured."""
    pass


def destroy_abr(abr):
    """Remove the 4 fields of the ABR with pop().
    Warning: at the end abr is a reference to an empty list []."""
    pass


#-------- The next function is used later to delete a node with a given key. --
def find_next_abr(sub_abr):
    """Find and return a subtree whose root key has a value that is the next
    one of val_abr(sub_abr). Return None if it is the maximum value.
    Note that the result is necessarily in this sub_abr."""
    pass


#------- This fonction is used to delete a node with a given value. -----------
def delete_val_abr(val, abr):
    """Find any key with value val and delete it form abr.
    If the value val is not in the ABR, only a warning message is printed.
    IMPORTANT: the modification is in place but the function returns the new
    reference on the new ABR since the root may change.
    Usage should be of the form: abr = delete_val_abr(10, abr)."""
    def delete_key_subabr_abr(sub_abr):
        """Delete the key at the root of the sub_abr in the ABR. """
        nonlocal abr  # The root of ABR may change during deletion.
    pass

    pass


class ValueNotInAbr(Exception):
    pass


def find_next_key_abr(val, abr):
    """Find and return the key of ABR whose value is the next one of val.
    Return None if val is the maximum value of the ABR.
    Raise ValueNotInAbr exception if the value is not in the ABR."""
    pass


#----------- Tests --------------
abr_global = create_abr((20, "A"))
print_abr(abr_global)
insert_abr((10, "B"), abr_global)
print_abr(abr_global)
insert_abr((15, "C"), abr_global)
print_abr(abr_global)
insert_abr((40, "D"), abr_global)
print_abr(abr_global)
insert_abr((25, "E"), abr_global)
print_abr(abr_global)
insert_abr((10, "F"), abr_global)  # Support many equal values.
print_abr(abr_global)
insert_abr((30, "G"), abr_global)
print_abr(abr_global)
abr_global = delete_val_abr(10, abr_global)
print_abr(abr_global)
abr_global = delete_val_abr(20, abr_global)
print_abr(abr_global)
insert_abr((100, "Z"), abr_global)
print_abr(abr_global)

print(f"The min key of the current ABR is: {find_minimum_key_abr(abr_global)}")
print(f"The max key of the current ABR is: {find_maximum_key_abr(abr_global)}")
print(f"The list of keys is {list_of_keys_abr(abr_global)}")
print(f"The ABR contains {len_abr(abr_global)} elements")
print(f"Key of the next value of 15 is {find_next_key_abr(15, abr_global)}")
pretty_print_abr(abr_global, 0)
print(f"Is ABR coherent? {is_coherent_abr(abr_global)}")

print("------ Test of iterator ------")
it = iter_on_keys_abr(abr_global)
for x in it:
    print(x)
