
### Data definition file for Graph G=(V,E) and Digraph G=(N,A).

### Data Definitions:
## A Node u is represented by an integer from 1 to n, the max number of nodes, or some other types (strings, etc.).
## A Vertex u is equivalent to Node, but defined in undirected graphs.
## An Arc ij is a Pair of Node, Arc(i, j), where i is tail and j is head
## An Edge ij is equivalent to Arc, but defind in undirected graphs.
## A Path is a sorted list of Edge [v1v2, v2v3, ..., vk-1vk], and no duplicates.
## A Cycle is a Path such that v1 = vk.
## A Dipath is a sorted list of Arc [v1v2, v2v3, ..., vk-1vk], and no dups.
## A Dicycle is a Dipath except for v1 = vk.
## An OrienCycle is oriented cycle such that edges are arcs, in either direction.
## An OrienPath is oriented path such that edges are arcs, in either direction.

## A Tree holds the following properties:
## 1. Connected and has no cycles
## 2. There is a unique path between any two vertices in Tree
## 3. |E| = |N| - 1
## 4. For an oriented Tree, if any node has out-degree of at least 1 then it
##    contains a dicycle.

## In a tree, there exists a unique ij-path for any two vertices i, j.
## Adding an edge to a tree will create a unique cycle, and removing any edge in that cycle will create a tree.
## (Thm 1.3) Let S be a st-cut in the graph. This important thoerm implies that there exists an st-dipath
## if and only if all st-cuts are non-empty.

### ***This constraint applies to all functions below***
### For any input graph/digraph, namely set of vertices/nodes and set of edges/arcs, they are matched (i.e. they can form a valid tree)
### Constraints involving endpoints of all edges/arcs are contained in the set of vertices/nodes.




class Edge:
    """
    A data definition for an edge ij. It is represented in algebraic order, that
    i is the small vertex, j is the large vertex.
    
    Fields: __first
            __second
    
    Features: CANNOT mutate this edge after initialization.
    
    """
    def __init__(self, vertex_1, vertex_2):
        """
        Edge(vertex_1, vertex_2) creats a new Edge.
        __init__: Vertex Vertex -> Edge
        Requires: vertex_1, vertex_2 are distinct.
        
        """
        assert vertex_1 != vertex_2, "Not Valid Edge"
        self.__first = min(vertex_1, vertex_2)
        self.__second = max(vertex_1, vertex_2)
    
    def __repr__(self):
        """
        repr(self) returns a string representing this edge, in algebraic order.
        __repr__: Edge -> Str
        
        """
        return str(self.__first) + "-" + str(self.__second)
    
    def first(self):
        """
        self.first() returns the small vertex index in self.
        first: Edge -> Vertex
        
        """
        return self.__first
    
    def second(self):
        """
        self.second() returns the large vertex index in self.
        second: Edge -> Vertex
        
        """
        return self.__second
    
    def vertices(self):
        """
        self.vertices() returns the endpoints of this edge.
        vertices: Edge -> (setof Vertex)
        
        """
        return set({self.__first, self.__second})
    
    def other(self, vertex):
        """
        self.other(vertex) returns the other node in self. False otherwise.
        other: Edge Vertex -> (anyof Vertex False)

        """
        if self.__first == vertex:
            return self.__second
        elif self.__second == vertex:
            return self.__first
        else:
            return False
    
    def __contains__(self, vertex):
        """
        vertex in self: returns true if vertex is one of the endpoints.
        __contains__: Edge Vertex -> Bool
        
        """
        return vertex == self.__first or vertex == self.__second
    
    def __eq__(self, other):
        """
        self == other: returns true if they are equivalent, False otherwise.
        __eq__: Edge Edge -> Bool
        
        """
        return self.__first == other.first() and self.__second == other.second()
        
    def __lt__(self, other):
        """
        self < other.
        __lt__: Edge Edge -> Bool
        
        """
        if self.__first == other.first():
            return self.__second < other.second()
        else:
            return self.__first < other.first()
        
    def __gt__(self, other):
        """
        self > other.
        __gt__: Edge Edge -> Bool
        
        """
        if self.__first == other.first():
            return self.__second > other.second()
        else:
            return self.__first > other.second()
        
    def __le__(self, other):
        """
        self <= other.
        __le__: Edge Edge -> Bool
        
        """
        return self < other or self == other
    
    def __ge__(self, other):
        """
        self >= other.
        __ge__: Edge Edge -> Bool
        
        """
        return self > other or self == other
    
    def __hash__(self):
        """
        returns the hash value.
        
        """
        return hash(self.__repr__())

def cut(vertices, edges):
    """
    cut(nodes, edges) returns the cut induced by nodes.
    cut: (setof Vertex) (setof Edge) -> (setof Edge)
    Cost: O(nm), n is the number of vertices, m is the number of edges.
    
    """
    cut = set()
    for edge in edges:
        if edge.vertices().issubset(vertices):
            continue
        elif edge.first() in vertices or edge.second() in vertices:
            cut.add(edge)
        else:
            continue
    return cut

def incident_edges(edges, v):
    """
    incident_edges(edges, v) returns the set of edges in edges with one endpoint v.
    incident_edges: (setof Edge) Vertex -> (setof Edge)
    Cost: O(m), m is the number of edges.

    """
    return {edge for edge in edges if v in edge}

def neighbours(edges, v):
    """
    neighbours(edges, vertex) returns the vertices that are incident to v.
    neighbours: (setof Edge) Vertex -> (setof Vertex)
    Cost: O(m), m is the number of edges in edges.

    """
    return {edge.other(v) for edge in edges if not edge.other(v) is False}
    
        
def if_connected(edges, vertices):
    """
    if_connected(edges, vertices) detects if the input graph is connected.
    This program uses BFS logic to traverse all nodes.

    Method 1: Find ij-path for all vertices i, j (too slow and not recommended)
    Method 2: BFS with colors to explore all vertices.

    if_connected: (setof Edge) (setof Vertex) -> Bool
    Cost: O()
    
    """
    

def if_tree(edges, vertices):
    """
    if_tree(edges, vertices) tells if arcs is a tree.
    Could be used for digraph as well.
    i.e. |E| == |V| - 1 (tree property 3)
    if_tree_flow: (setof Edge) (setof Vertex) -> Bool
    Cost: O(n+m), n is the number of nodes and m is the number of m
    
    """
    return len(edges) == len(vertices) - 1




"""
2 ideas for find_path:
1:
1. Take in edges, transfer them into a huge set of arcs where each edge is mapped to 2 directed arcs.
2. Find any ij-dipath.
3. Transfer this dipath into path.

2: Fit the code for find_dipath to find_path.

PesudoCode:
1:
edge_to_arc(edge):
    return {Arc(edge.first(), edge.second()), Arc(edge.second(), edge.first())}

edges_to_arcs(edges):
    arcs = set()
    for edge in edges:
        arcs |= edge_to_arc(edge)
    return arcs

find_path(Edges, i, j):
    arcs = edges_to_arcs(Edges)
    dipath = find_dipath(arcs, i, j)
    result = arcs_to_edges(dipath)

"""

### method 2
def find_path(edges, i, j, visited_v = None, length = 0, avoid_edges = None, process = False):
    """
    finds an ij-path in the graph. Might have distinct results depending on the order of traversal, and False otherwise.
    for trees, will only give one unique ij-path.
    use DFS logic.
    find_path: (setof Edge) Vertex Vertex Edge (setof Vertex) Bool -> (anyof Path False)
    Requires: not used for finding cycle.
    Cost: O()

    """
    assert i != j, "cannot use for cycle"
    if visited_v is None:
        visited_v = set()
    visited_v.add(i)
    i_cut = incident_edges(edges, i)
    #new_visited = visited_v.copy()
    #new_visited.add(i)
    if process:
        print("-------------------------------")
        print(f"Finding {i},{j}-path:")
        print(f"length from starting: {length}")
        print(f"visited vertices: {visited_v}")
        print(f"traverse cut [{i}]: {i_cut}")
        print("-------------------------------")
    for edge in i_cut:
        if process:
            print(f">>>>>>now on edge {edge}")
        if not avoid_edges is None:
            if edge in avoid_edges:
                if process:
                    print(f"avoid {edge}")
                continue
        if edge.other(i) == j:
            if process:
                print(f"target ({j}) is found on {edge}. success")
            return [edge]
        elif not edge.other(i) in visited_v:
            if process:
                print(f"target ({j}) not found on {edge}. keep walking along this edge")
            rest = find_path(edges, edge.other(i), j, visited_v, length + 1, avoid_edges, process)
            if not rest is False:
                if process:
                    print(f"adding {edge} before {rest}")
                return [edge] + rest
            else:
                if process:
                    print(f"cut [{i}] edge {edge} failed. next")
                continue
        else:
            if process:
                print(f"head {edge.other(i)} is visited. skipping this edge {edge}")
            continue
    return False

### plain pesudo code:
"""
find_path(edges, i, j, visited_v = set(), process = False):
    i_cut = incident_edges(edges, i)
    new_visited = visited_v.copy()
    new_visited.add(i)
    for edge in i_cut:
        if edge.other(i) == j:
            return [edge]
        elif not edge.other(i) in new_visited:
            rest = find_path(edges, edge.other(i), j, new_visited, process)
            if not rest is False:
                return [edge] + rest
            else:
                continue
        else:
            continue
    return False
"""









class Arc:
    """
    A data definition for an arc ij.
    Fields: __tail (Node)
            __head (Node)
            
    Features: CANNOT mutate this arc after initialization.
    
    """
    def __init__(self, tail, head):
        """
        Arc(tail, head) creates an arc
        __init__: Node Node -> Arc
        Requires: tail != head
        
        """
        assert tail != head, "Not Valid Arc"
        self.__tail = tail
        self.__head = head
        
    def head(self):
        """
        self.head() returns the head of this arc
        head: -> Node
        
        """
        return self.__head
    
    def tail(self):
        """
        self.tail() returns the tail of this arc
        tail: -> Node
        
        """
        return self.__tail
    
    def __repr__(self):
        """
        repr(self) generates a string representation for this arc
        repr: -> Str
        
        """
        return str(self.__tail) + "->" + str(self.__head)
    
    def head_or_tail(self, node):
        """
        self.head_or_tail(node) returns -1 if node is the tail, 1 if node is the
                head, and 0 if this arc does not contain this node
        head_or_tail: Node -> (anyof 1 0 -1)
        
        """
        if self.__tail == node:
            return -1
        elif self.__head == node:
            return 1
        else:
            return 0
        
    def __contains__(self, node):
        """
        node in self produces true if node is in this arc
        __contains__: Node -> Bool
        
        """
        return self.head_or_tail(node) != 0
    
    def __eq__(self, other):
        """
        self == other returns True if they are equivalent, False otherwise
        __eq__: Arc Arc -> Bool
        
        """
        return (self.__tail == other.tail()) and \
               (self.__head == other.head())
    
    def __lt__(self, other):
        """
        self < other: Compare the algebraic order.
        __lt__: Arc Arc -> Bool
        
        """
        if self.__tail == other.tail():
            return self.__head < other.head()
        else:
            return self.__tail < other.tail()
        
    def __gt__(self, other):
        """
        self > other: Compare the algebraic order.
        __gt__: Arc Arc -> Bool
        
        """
        if self.__tail == other.tail():
            return self.__head > other.head()
        else:
            return self.__tail > other.tail()
        
    def __le__(self, other):
        """
        self <= other: Compare the algebraic order.
        __le__: Arc Arc -> Bool
        
        """
        return self < other or self == other
    
    def __ge__(self, other):
        """
        self >= other: Compare the algebraic order.
        __ge__: Arc Arc -> Bool
        
        """
        return self > other or self == other
        
    def __hash__(self):
        """
        numerical/string value of tail and head to represent itself
        
        """
        #return hash(10 * self.__tail + self.__head)
        return hash(self.__repr__())
        
        

## Examples:
### feasible TP
arc12 = Arc(1, 2)
arc13 = Arc(1, 3)
arc15 = Arc(1, 5)
arc23 = Arc(2, 3)
arc24 = Arc(2, 4)
arc34 = Arc(3, 4)
arc45 = Arc(4, 5)
ini_Nodes = {1, 2, 3, 4, 5}
ini_Demands = {1: -5, 2: -2, 3: -7, 4: 8, 5: 6}
ini_Arcs = {Arc(1, 2), Arc(1, 3), Arc(1, 5), Arc(2, 3), Arc(2, 4), Arc(3, 4), \
            Arc(4, 5)}
ini_Costs = {Arc(1, 2): 1, Arc(1, 3): 7, Arc(1, 5): 1, Arc(2, 3): 1, \
            Arc(2, 4): 8, Arc(3, 4): 9, Arc(4, 5): 3}
ini_flow = {Arc(1, 3): 5, Arc(2, 4): 2, Arc(3, 4): 12, Arc(4, 5): 6}
ini_Tree = set(ini_flow.keys())

def incident_arcs(node, arcs):
    """
    incident_arcs(node, arcs) returns a set of Arc that are incident to node.
    incident_arcs: Node (setof Arc) -> (setof Arc)
    
    """
    """
    result = set()
    for arc in arcs:
        if node in arc:
            result.add(arc)
    """
    return {arc for arc in arcs if node in arc}

def head_arcs(node, arcs):
    """
    head_arcs(node, arcs) returns a set of arcs with head node.
    head_arcs: Node (setof Arc) -> (setof Arc)
    Cost: O(m), m is the number of arcs
    
    """
    """
    result = set()
    for arc in arcs:
        if arc.head_or_tail(node) == 1:
            result.add(arc)
    """
    return {arc for arc in arcs if arc.head_or_tail(node) == 1}

def tail_arcs(node, arcs):
    """
    tail_arcs(node, arcs) returns a set of arcs with tail node.
    head_arcs: Node (setof Arc) -> (setof Arc)
    Cost: O(m), m is the number of arcs
    
    """
    """
    result = set()
    for arc in arcs:
        if arc.head_or_tail(node) == -1:
            result.add(arc)
    """

    return {arc for arc in arcs if arc.head_or_tail(node) == -1}  

def dicut(nodes, arcs):
    """
    dicut(nodes, arcs) returns the cut of arcs induced by nodes.
    dicut: (setof Node) (setof Arc) -> (setof Arc)
    Cost: O(nm), n is the number of nodes, m is the number of arcs
    
    """
    """
    dicut = set()
    for arc in arcs:
        if (arc.tail() in nodes) and (not arc.head() in nodes):
            dicut.add(arc)
    """
    dicut = {arc for arc in arcs if (arc.tail() in nodes) and \
             (not arc.head() in nodes)}
    return dicut

def arc_to_edge(arc):
    """
    arc_to_edge(arc) transforms an Arc to Edge.
    arc_to_edge: Arc -> Edge
    
    """
    return Edge(arc.head(), arc.tail())

def arcs_to_edges(arcs):
    """
    arcs_to_edges(arcs) transforms a set of Arc into Edge.
    arcs_to_edges: (setof Arc) -> (setof Edge)
    Cost: O(m), m is the number of arcs.
    
    """
    return {arc_to_edge(arc) for arc in arcs}

def arcs_to_nodes(arcs):
    """
    arcs_to_nodes(arcs) transforms arcs to nodes.
    arcs_to_nodes: (setof Arc) -> (setof Node)
    Cost: O()

    """
    nodes = set()
    for arc in arcs:
        nodes.add(arc.tail())
        nodes.add(arc.head())
    return nodes

def dipath_to_nodes(dipath):
    """
    dipath_to_nodes(dipath) consumes a dipath and converts it to nodes.
    dipath_to_nodes: Dipath -> (listof Node)
    Cost: O(n), n is the number of arcs in dipath.

    """
    nodes = []
    length = len(dipath)
    for i in range(length):
        nodes.append(dipath[i].tail())
        if i == (length - 1):
            nodes.append(dipath[i].head())
    return nodes

def path_compare(path1, path2):
    '''
    Compare two paths by:
    1. length
    2. lexicographic order
    
    '''
    if len(path1) < len(path2):
        return -1
    elif len(path1) > len(path2):
        return 1
    else:
        for i in range(len(path1)):
            if path1[i] < path2[i]:
                return -1
            elif path1[i] > path2[i]:
                return 1
            else:
                continue
    return 0

def find_dipath(arcs, i, j, visited_nodes = None, limit = None, length = 0, avoid_arcs = None, avoid_nodes = None, process = False):
    """
    find_dipath(arcs, i, j, visited_nodes, limit, length, avoid_arcs, process) finds a ij-dipath in the graph with DFS logic. Will return a list of ordered arcs as a path if found.
    Will return False otherwise. Will avoid using edges in avoid_arcs. Will track the length from starting point. Will stop searching if exceed the length limit.
    will print searching process if process is on.
    The program is designed to handle digraphs with dicycles.
    Could give different results if multiple ij-dipaths exist, depending on the first found dipath.
    If the input is a tree, there exists a unique dipath if any.
    Requires: Cannot find dicycle. i != j. i, j not in avoid_nodes.
    Input: arcs, visited_nodes, avoid_edges are sets of arcs
    """
    assert i != j, "cannot use for dicycle"
    if not limit is None:
        if length >= limit:
            if process:
                print("exceed length limit")
            return False
    ### initialize set for each new call
    if visited_nodes is None:
        visited_nodes = set()
    i_cut = tail_arcs(i, arcs)
    visited_nodes.add(i)
    #visited_nodes.add(i)
    if process:
        print(f"finding {i},{j}-dipath:")
        print(f"length from starting: {length}")
        print(f"visited nodes: {visited_nodes}")
        print(f"avoid using arcs: {avoid_arcs}")
        print(f"avoid using nodes: {avoid_nodes}")
        print(f"traversing cut [{i}]: {i_cut}")
    ### traverse the cut
    for arc in i_cut:
        if process:
            print(f"on arc {arc}")
        ### check if to avoid
        if not avoid_arcs is None:
            if arc in avoid_arcs:
                if process:
                    print(f"avoid using arc {arc}")
                continue
        if not avoid_nodes is None:
            if arc.head() in avoid_nodes:
                if process:
                    print(f"avoid using node {arc.head()}")
                continue
        ### journal ends. successful search
        if arc.head_or_tail(j) == 1:
            if process:
                print(f"target ({j}) found on {arc}")
            return [arc]
        ### not matched. keep going along this arc
        else:
            if process:
                print(f"target ({j}) not found on {arc}. keep walking along this arc")
            ### the head is visited before. prevent cycles
            if arc.head() in visited_nodes:
                if process:
                    print(f"head {arc.head()} is visited. skipping this arc.")
                continue
            ### head is not visited. keep going
            rest = find_dipath(arcs, arc.head(), j, visited_nodes, limit, length + 1, avoid_arcs, avoid_nodes, process)
            ### this arc uv's head v can approach j, where exists a "successful vj-dipath" in the graph
            if not rest is False:
                if process:
                    print(f"adding {arc} before {rest}")
                ### add this arc into the path, as the previous arc precceding the "successful rest dipath"
                return [arc] + rest
            ### not found a dipath from this arc's head to j
            else:
                if process:
                    print(f"cut [{i}] arc {arc} failed. next")
                ### keep searching along other arcs in the cut
                continue
    ### search through all cut arcs failed.
    return False

def if_reachable(arcs, i, j, length_lim = None):
    """
    if_reachble(arcs, i, j, length) detects if j is reachable from i with length limit.
    if_reachable: (setof Arc) Node Node (anyof Int None) -> Bool

    """
    dipath = find_dipath(arcs, i, j, limit = length_lim)
    return not dipath is False

def reachable_from(arcs, i, length = None):
    """
    reachable_from(arcs i) returns a set of nodes that are reachable from i in length long.
    reachable_from: (setof Arc) Node (anyof Int None) -> (setof Node)

    """
    nodes = arcs_to_nodes(arcs)
    return {node for node in nodes if i != node and if_reachable(arcs, i, node, length)}

def reachable_to(arcs, i, length = None):
    """
    reachable_to(arcs, i) returns a set of nodes that can reach i in length long.
    reachable_to: (setof Arc) Node (anyof Int None) -> (setof Node)

    """
    nodes = arcs_to_nodes(arcs)
    return {node for node in nodes if i != node and if_reachable(arcs, node, i, length)}

def print_paths(paths):
    """
    print_paths(paths) prints the paths/dipaths pretty.
    print_paths: (listof Path/Dipath) -> None
    Effects: prints paths
    Cost: O(n), n is the number of paths in paths.

    """
    length = len(paths)
    count = 0
    print(f"Found {length} paths in total:")
    for path in paths:
        print(f"Path {count + 1}: {paths[count]}")
        count += 1

def all_disjoint_dipaths(arcs, i, j, limit = None, if_print = False):
    """
    all_disjoint_paths(edges, i, j, limit, if_print) returns all disjoint dipaths between i, j in a list.
    all_paths: (setof Arc) Vertex/Node Node Bool -> (listof Dipath)

    the output is not unique, which depends on the order of visited arcs.

    Effects: might print paths
    Cost: as well as the cost of finding an ij-dipath.

    """
    result = []
    avoid = set()
    while True:
        dipath = find_dipath(arcs, i, j, limit = limit, avoid_arcs = avoid)
        if dipath is False:
            break
        result.append(dipath)
        avoid |= set(dipath)
        #dipath = find_dipath(arcs, i, j, avoid_arcs = avoid)
    if if_print:
        print_paths(result)
    return result



def find_dicycle(arcs, i, limit = None, length = 0, avoid_arcs = None, process = False):
    """
    finds the dicycle that passes i.

    """

    ### method 1
    """
    if not limit is None:
        if length >= limit:
            if process:
                print("exceed length limit")
            return False
    if visited_nodes is None:
        visited_nodes = set()
    visited_nodes.add(i)
    i_cut = tail_arcs(i, arcs)
    if process:
        print(f"finding dicycle containing {i}: ")
        print("visited nodes")
    for arc in i_cut:
        if arc.head() == i:
            return [arc]
        elif arc.head() in visited_nodes:
            continue
        ...
    """

    ### method 2
    i_cut = tail_arcs(i, arcs)
    if process:
        print(f"cut [{i}]: {i_cut}")
        if not bool(i_cut):
            print(f"no dicycles containing {i}")
    for arc in i_cut:
        if process:
            print(f"on arc {arc}:")
        dipath = find_dipath(arcs, arc.head(), i, limit = limit, avoid_arcs = avoid_arcs, process = process)
        if dipath is False:
            if process:
                print(f"no {arc.head()},{i}-dipath exists. skipping arc {arc}")
            continue
        else:
            if process:
                print(f"found {arc.head()},{i}-dipath. adding {arc} before")
            return [arc] + dipath
    return False

def find_all_dipaths_dicycles(arcs, i, j, visited_nodes = None, result = None, temp_dipath = None, limit = None, length = 0, avoid_arcs = None, avoid_nodes = None, process = False):
    """
    find all dipaths/dicycles from i to j.
    First find cut at i, then find vj-dipath for all arc iv in cut at i.
    Requires: result is a valid list. i, j not in avoid nodes.
    Effects: will mutate the input result.
    Features: the ouput is unique, regardless the order of dipaths found. Can use for finding dicycles.
    """

    """
    i_cut = tail_arcs(i, arcs)
    for arc in i_cut:
        dipath = find_dipath(arcs, arc.head(), j)
    """

    """
    if result is None:
        result = set()
    i_canreach = reachable_from(arcs, i)
    canreach_j = reachable_to(arcs, j)
    middle = i_canreach & canreach_j
    """
    #assert i != j, "cannot use for dicycle"
    if limit is not None:
        if length >= limit:
            if process:
                print("exceed length limit")
            return False
    if temp_dipath is None:
        temp_dipath = []
    if result is None:
        result = []
    if visited_nodes is None:
        visited_nodes = set()
    visited_nodes.add(i)
    #new_visited = visited_nodes.copy()
    #new_visited.append(i)
    i_cut = tail_arcs(i, arcs)
    if process:
        print(f"finding {i},{j}-dipath:")
        print(f"cut [{i}]: {i_cut}")
        print(f"current dipath: {temp_dipath}")
        print(f"visited nodes: {new_visited}")
        print(f"visited/found wanted dipaths: {result}")
        print(f"length from start: {length}")
        print(f"length limit: {limit}")
        print(f"avoid arcs: {avoid_arcs}")
        print(f"avoid nodes: {avoid_nodes}")
    for arc in i_cut:
        if process:
            print(f">>>>>>>>>>>>> now on arc {arc}")
        if avoid_arcs is not None:
            if arc in avoid_arcs:
                if process:
                    print(f"avoid using arc {arc}")
                continue
        if avoid_nodes is not None:
            if arc.head() in avoid_nodes:
                if process:
                    print(f"avoid using node {arc.head()}")
                continue
        if arc.head() == j:
            if process:
                print(f"found dipath ending ({j}). adding {arc} after {temp_dipath}")
            result.append(temp_dipath + [arc])
            continue
            #return True
        if process:
            print(f"target ({j}) is not found on {arc}. next")
        if arc.head() in visited_nodes:
            if process:
                print(f"{arc.head()} is visited. skipping this arc {arc}")
            continue
        temp_dipath.append(arc)
        find_all_dipaths_dicycles(arcs, arc.head(), j, visited_nodes, result, temp_dipath, limit, length + 1, avoid_arcs, avoid_nodes, process)
        temp_dipath.remove(arc)
    visited_nodes.remove(i)
    #return False

def all_dipaths(arcs, i, j, limit = None, avoid_arcs = None, avoid_nodes = None, if_print = False, process = False):
    """
    beautiful wrapper function for find_all_dipaths_dicycles to find dipaths.
    can choose to print

    features: the output is unique
    Requries: i, j distinct.
    """
    assert i != j, "cannot use for dicycle"
    result = []
    find_all_dipaths_dicycles(arcs, i, j, result = result, limit = limit, avoid_arcs = avoid_arcs, avoid_nodes = avoid_nodes, process = process)
    if if_print:
        print(f"finding {i},{j}-dipath:")
        print(f"length limit: {limit}")
        print(f"avoid arcs: {avoid_arcs}")
        print(f"avoid nodes: {avoid_nodes}")
        print_paths(result)
    return result

def all_dicycles(arcs, i, limit = None, avoid_arcs = None, avoid_nodes = None, if_print = False, process = False):
    """
    beautiful wrapper function for find_all_dipaths_dicycles to find dicycles.
    can choose to print

    features: the output is unique

    """
    result = []
    find_all_dipaths_dicycles(arcs, i, i, result = result, limit = limit, avoid_arcs = avoid_arcs, avoid_nodes = avoid_nodes, process = process)
    if if_print:
        print(f"finding dipath containing {i}:")
        print(f"length limit: {limit}")
        print(f"avoid arcs: {avoid_arcs}")
        print(f"avoid nodes: {avoid_nodes}")
        print_paths(result)
    return result

### These are not an efficient way to find dipaths/dicycles. Improvement Idea: consider middle nodes that are reachable from i or to j.