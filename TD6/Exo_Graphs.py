import random
# import Special_Graphs

"""A vertex is a string.
A graph is a dictionary; its keys are vertices and the value associated to a
key/vertex u is the set of neighbors of u in G."""

def extract_graph_from_file(file):
    """Takes a file name as input and extracts the graph inside it.
    The file is composed of n lines, where n is the total number of vertices.
    Each line is of the form u:v1:v2:...:vk where u is a vertex and the
    vi's are its neighbors. If u has no neighbor, the corresponding line is u:
    This function returns a dictionary representing the graph:
    Its keys are vertices and its values are the sets of neighbors
    of each vertex. """
    graph = dict()
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line[:-1].split(':')
            graph[line[0]] = set(line[1:])
    return graph

def set_of_vertices(graph):
    """Returns the set of vertices of the graph."""
    return set(graph.keys())

def set_of_neighbors(graph, u):
    """Returns the set of neighbors of vertex u in the graph."""
    return graph[u]

def degree_of(graph, u):
    """Returns the numbers of neighbors of vertex u in the graph."""
    return len(set_of_neighbors(graph, u))

def are_neighbors(graph, u, v):
    """Boolean function returning True if u and v are neighbors in the graph.
     Returns False otherwise."""
    return v in set_of_neighbors(graph, u)

def number_of_vertices(graph):
    """Returns the number of vertices of the graph."""
    return len(set_of_vertices(graph))

def number_of_edges(graph):
    """Returns the number of edges of the graph.
    We suppose that it is NON directed."""
    count = 0
    for vertex in set_of_vertices(graph):
        count += len(set_of_neighbors(graph, vertex))
    return int(count/2)
    """m = sum(degree_of(graph, u) for u in set_of_vertices(graph))
    return m//2"""

def is_symmetric(graph):
    """Boolean function returning True if the dictionary representing the graph
    is symmetric: u is a neighbor of v iff v is a neighbor of u.
    Returns False otherwise and print a non symmetric couple."""
    for vertex in set_of_vertices(graph):
        for neighbor in set_of_neighbors(graph, vertex):
            if not are_neighbors(graph, neighbor, vertex):
                return False
    return True

def bfs(graph, r):
    """Makes the BFS of the graph from vertex r. Returns a tuple
    (parent, d, color)."""
    d = {x:None for x in set_of_vertices(graph)}
    pi = {x:None for x in set_of_vertices(graph)}
    couleur = {x:None for x in set_of_vertices(graph)}
    
    for vertex in set_of_neighbors(graph, r):
        if vertex != r:
            couleur[vertex] = 'BLANC'
            d[vertex] = 999
            pi[vertex] = None
    couleur[r] = 'GRIS'
    d[r] = 0
    pi[r] = None
    queue = []
    queue.append(r)
    
    while len(queue) > 0 :
        sommet = queue[0]
        for neighbor in set_of_neighbors(graph, sommet):
            if couleur[neighbor] == 'BLANC':
                couleur[neighbor] = 'GRIS'
                d[neighbor] = d[sommet] + 1
                pi[neighbor] = sommet
                queue.append(neighbor)
        queue.pop(0)
        couleur[sommet] = 'NOIR'
    return (pi, d, couleur)

def color_graph_by_list(graph, list_of_vertices):
    """Takes as input a graph and a list of its vertices. This function colors
    the graph with this list and returns a tuple (c, color) where:
     + color is the constructed coloration (a dictionary whose keys are the
     vertices and values are colors (integers > 0)) and
     + c is the number of colors used by the coloration color."""
    color = {x:0 for x in list_of_vertices}
    for vertex in list_of_vertices:
        for neighbor in set_of_neighbors(graph, vertex):
            if color[vertex] == color[neighbor]:
                color[vertex] += 1
    return color
    """color = {u: None for u in list_of_vertices}
    n = number_of_vertices(graph)
    for u in list_of_vertices:
        colors_of_neighbors = set(color[v] for v in set_of_neighbors(graph, u))
        colors_of_neighbors.discard(None)
        color[u] = min(set(range(1, n+1)).difference(colors_of_neighbors))
    return len(set(color.values())), color"""

def color_graph_by_random_lists(graph, number_of_iterations=1):
    """Takes as input a graph, and an integer number_of_iterations.
    Runs number_of_iterations times the coloring function of the graph on
    random lists of vertices of the graph and returns the best coloring found
    (the one using the lowest number of colors)."""
    pass


def is_stable(graph, set_s):
    """Boolean function taking as input a graph and a set of vertices.
    It returns True if this set is a stable of the graph (there is no edge
     between vertices of this set in the graph).
     Returns False otherwise."""
    pass


def is_proper_coloring(graph, color):
    """Takes as input a graph and a coloring (a dictionary having the set of
    vertices as keys and colors (integers > 0) as values).
    Returns True if color is a proper coloring of the graph.
    Returns False otherwise and print a message to indicate the error."""
    pass


# Special_Graphs.hypercube_graph(3)  # To construct a hypercube(d)
global_graph = extract_graph_from_file("H3")
print("------ BFS from 000:", bfs(global_graph, "000"))
print(f"------ Is the graph symmetric? {is_symmetric(global_graph)}")
global_coloring_of_the_graph = color_graph_by_random_lists(global_graph, 4)
print(global_coloring_of_the_graph)
# resultG["000"] = resultG["010"] # To force an error in H3 graph.
print(f"-- Is it a valid coloring? "
      f"{is_proper_coloring(global_graph, global_coloring_of_the_graph)}")

# Personnal Test #

print(f"Set of graph vertices : {set_of_vertices(global_graph)}")

print(f"Set of neighbor with vertex '000': {set_of_neighbors(global_graph, '000')}")

print(f"Degree of '000' in graph: {degree_of(global_graph, '000')}")

print(f"Are neighbors ? '000' '110': {are_neighbors(global_graph, '000', '110')}")
print(f"Are neighbors ? '000' '010': {are_neighbors(global_graph, '000', '010')}")

print(f"Number_of_vertices : {number_of_vertices(global_graph)}")

print(f"Number of edges : {number_of_edges(global_graph)}")

print(f"Is a symetric graph: {is_symmetric(global_graph)}")

print(f"bfs: {bfs(global_graph, '000')}")

print(f"color graph: {color_graph_by_list(global_graph, list(set_of_vertices(global_graph)))}")
