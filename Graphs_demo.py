### Draft functions, Demo and Tests for Graph.py.
from Graphs import *

### Draft functions.
"""
def is_cycle_or_path(edges):
    
    is_cycle(edges) detects if the input set of edges is a cycle/path.
    If it's path, will return (0, Path).
    If it's cycle, will return (1, Cycle).
    If neigher, will return False.
    is_cycle: (setof edges) -> (anyof (0, Path) (1, Cycle) False)
    Requires: edges non-empty
    Cost: O(m), m is the number of edges.
    
    sorted_edges = sorted(edges)
    length = len(edges)
    
    if length <= 2:
        return False
    
    head = sorted_edges[0].first()
    for i in range(0, length):
        ### last edge
        if i == length - 1:
            ### cycle
            if sorted_edges[i].second() == head:
                return (1, sorted_edges)
            ### path
            else:
                return (0, sorted_edges)
        else:
            if sorted_edges[i].second() == sorted_edges[i + 1].first():
                continue
            else:
                return False
"""


"""
### wrong logic
def is_cycle(edges):
    
    is_cycle(edges) detects if the input set of edges is a cycle, and will
        return a Cycle if found, and False otherwise.
    is_cycle: (setof edges) -> (anyof Cycle False)
    Requires: edges non-empty and no duplicate edges
    Cost: O(m), m is the number of edges.
    
    
    sorted_edges = sorted(edges)
    length = len(edges)
    if length <= 2:
        return False
    start = sorted_edges[0].first()
    for i in range(length):
        ### last edge
        if i == length - 1:
            ### cycle
            if sorted_edges[i].second() == start:
                return sorted_edges
            else:
                return False
        else:
            if sorted_edges[i].second() == sorted_edges[i + 1].first():
                continue
            else:
                return False    


def is_path(edges):
    
    is_path(edges) detects if edges is a Path and returns it, and False otherwise.
    is_path: (setof Edge) -> (anyof Path False)
    Requires: edges non-empty
    Cost: O(m), m is the number of edges.
    
    
    sorted_edges = sorted(edges)
    length = len(edges)
    if length == 1:
        return sorted_edges
    start = sorted_edges[0].first()
    for i in range(length):
        ### last edge
        if i == length - 1:
            ### path
            if sorted_edges[i].second() != start:
                return sorted_edges
            else:
                return False
        else:
            if sorted_edges[i].second() == sorted_edges[i + 1].first():
                continue
            else:
                return False    

"""


"""
def is_dicycle_or_dipath(arcs):
    
    is_dicycle(arcs) detects if a set of Arc is a dicycle/dipath.
    Dipath: returns 0 and a Dipath.
    is_dicycle: (setof Arc) -> (anyof (0, Dipath) (1, Dicycle) False)
    Cost: O(m), m is the number of arcs.
    
    
    sorted_arcs = sorted(arcs)
    length = len(sorted_arcs)
    start = sorted_arcs[0].tail()
    for i in range(0, length):
        if i == length - 1:
            s
"""

"""
def is_dipath(arcs):
    
    is_dipath(arcs) detects if arcs form a Dipath, and return it if any, False
        otherwise.
    is_dicycle: (setof Arc) -> (anyof Dipath False)
    Cost: O(m), m is the number of arcs.
    
    
    sorted_arcs = sorted(arcs)
    length = len(sorted_arcs)
    if length == 1:
        return True
    start = sorted_arcs[0].tail()
    for i in range(length):
        if i == length - 1:
            if sorted_arcs[i].head() != start:
                return sorted_arcs
            else:
                return False
        else:
            if sorted_arcs[i].head() == sorted_arcs[i + 1].tail():
                continue
            else:
                return False

def is_dicycle(arcs):
    
    is_dicycle(arcs) detects if arcs form a Dicycle, and return it if any, False
        otherwise.
    is_dicycle: (setof Arc) -> (anyof Dicycle False)
    Cost: O(m), m is the number of arcs.
    
    
    sorted_arcs = sorted(arcs)
    length = len(sorted_arcs)
    if length == 1:
        return False
    start = sorted_arcs[0].tail()
    for i in range(length):
        ### last arc
        if i == length - 1:
            if sorted_arcs[i].head() == start:
                return sorted_arcs
            else:
                return False
        else:
            if sorted_arcs[i].head() == sorted_arcs[i + 1].tail():
                continue
            else:
                return False

def is_oriencycle(arcs):
    
    is_oriencycyle(arcs) detects if arcs is an oriented cycle of arcs.
    is_oriencycle: (setof Arc) -> Bool
    Cost: O(m), m is the number of arcs
    
    
    edges = arcs_to_edges(arcs)
    return not is_cycle(edges) is False

def is_orienpath(arcs):
    
    O(m)
    
    edges = arcs_to_edges(arcs)
    return not is_path(edges) is False
"""

### TESTS & DEMO

### Tests on-off
TEST_EDGE = False ### test basic edge functions
TEST_EDGE_ADV = False ### test advanced edge functions
TEST_ARC = False
TEST_FIND_DIPATH = False
TEST_FIND_PATH = False
TEST_FIND_DIPATH_FUNS = False
TEST_FIND_DICYCLE = False
TEST_FIND_ALL_DIPATHS = False

### Basic Edge Function Tests
if TEST_EDGE:
    e12 = Edge(1, 2)
    e13 = Edge(1, 3)
    print("12 < 13: ", e12 < e13)
    e21 = Edge(2, 1)
    print("12 == 21: ", e12 == e21)
    print("edge 12, edge 21, edge 13: ", e12, e21, e13)

### Advanced Edge Function Tests
if TEST_EDGE_ADV:
    ini_Vertices = {1, 2, 3, 4}
    ini_Edges = {Edge(1, 2), Edge(1, 3), Edge(1, 4), Edge(2, 4), Edge(3, 4)}
    print()
    print("Vertices: ", ini_Vertices)
    print("Edges: ", ini_Edges)
    print("cut induced by {1, 2}: ", cut({1, 2}, ini_Edges))
    print("cut induced by {1, 2, 4}: ", cut({1, 2, 4}, ini_Edges))
    print()
    print("Neighbours of 1: ", neighbours({Edge(1, 2), Edge(1, 3), Edge(1, 4), Edge(2, 4), Edge(3, 4)}, 1))
    

    '''
    print("This is a path: 12, 23, 34: ", is_path({Edge(1, 2), Edge(2, 3), Edge(3, 4)}))
    print("This is not a path: 12, 13, 15: ", is_path({Edge(1, 2), Edge(1, 3), Edge(1, 5)}))
    print("This is not a path: 12, 23, 31: ", is_path({Edge(1, 2), Edge(2, 3), Edge(3, 1)}))
    print("This is not a path: 12, 13, 31: ", is_path({Edge(1, 2), Edge(1, 3), Edge(3, 1)}))
    print("This is a cycle 12, 13, 31: ", is_cycle({Edge(1, 2), Edge(1, 3), Edge(3, 1)}))
    '''
dipath1 = {Arc(1, 3), Arc(3, 5), Arc(5, 6)}
dipath2 = {Arc(1, 3), Arc(1, 5), Arc(2, 7)}
supergraph = {Arc(1, 2), Arc(1, 3), Arc(1, 5), Arc(2, 4), Arc(2, 5), Arc(3, 2), Arc(3, 9), Arc(3, 10), Arc(5, 10), Arc(10, 1)}
supergraph.add(Arc(2, 7))
supergraph.add(Arc(7, 5))
supergraph.add(Arc(5, 9))
cities = {Arc(1, 2), Arc(1, 3), Arc(2, 3), Arc(2, 4), Arc(3, 4), Arc(4, 1)}
#print("\n\n14-dipath: ", find_dipath(cities, 1, 4))
#all_dipaths(cities, 1, 4, if_print = True)
#all_dipaths(cities, 1, 4, limit = 2, if_print = True)

if TEST_FIND_DIPATH:
    print("dipath1: ", dipath1)
    print("find 16-dipath in dipath1: ", find_dipath(dipath1, 1, 6, process = True))
    print()
    print("find 35-dipath in dipath1: ", find_dipath(dipath1, 3, 5, process = True))
    print()
    print("find 36-dipath in dipath1: ", find_dipath(dipath1, 3, 6, process = True))
    print()
    print("no 45-dipath in dipath1: ", find_dipath(dipath1, 4, 5, process = True))
    print()
    print("no 24-dipath in dipath1: ", find_dipath(dipath1, 2, 4, process = True))
    print()
    
    print("dipath2: ", dipath2)
    print("no 17-dipath: ", find_dipath(dipath2, 1, 7, process = True))
    print()
    print("find 13-dipath: ", find_dipath(dipath2, 1, 3, process = True))
    print()
    print("find 56-dipath: ", find_dipath(dipath2, 5, 6, process = True))
    print()


    ### this graph contains some dicycles
    """
    supergraph = {Arc(1, 2), Arc(1, 3), Arc(1, 5), Arc(2, 4), Arc(2, 5), Arc(3, 2), Arc(3, 9), Arc(3, 10), Arc(5, 10), Arc(10, 1)}
    print("Supergraph: ", supergraph)
    print("find 12-dipath: ", find_dipath(supergraph, 1, 2, process = True))
    supergraph.add(Arc(2, 7))
    supergraph.add(Arc(7, 5))
    supergraph.add(Arc(5, 9))
    """
    #print("remove arc 12 from supergraph. then find 12-dipath: ", find_dipath(supergraph, 1, 2, process = True))

    #not allowed: print("find any 1,1-dicycle: ", find_dipath(supergraph, 1, 1, True))

    print("edited supergraph: ", supergraph)
    print("find 19-dipath: ", find_dipath(supergraph, 1, 9, process = True))
    print()
    print("no 18-dipath: ", find_dipath(supergraph, 1, 8, process = True))

    # version 1
    """
    def find_dipath(arcs, i, j, visited_nodes = set(), process = False):
        assert i != j, "cannot use for dicycle"
        i_cut = tail_arcs(i, arcs)
        #visited_nodes.add(i)
        if process:
            print(f"finding {i},{j}-dipath:")
            print(f"visited nodes: {visited_nodes}")
            print(f"traversing cut [{i}]: {i_cut}")
        ### traverse the cut
        for arc in i_cut:
            if process:
                print(f"on arc {arc}")
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
                ### do not interpret this visited_nodes. copy a new one for them
                new_visited = visited_nodes.copy()
                ### add i as visited
                new_visited.add(i)
                rest = find_dipath(arcs, arc.head(), j, new_visited, process)
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
        """
    ### version 1 tests
    ### Sample output 1
    """
    edited supergraph:  {3->2, 2->5, 1->2, 3->9, 10->1, 2->4, 2->7, 1->5, 3->10, 5->9, 5->10, 1->3, 7->5}

    finding 1,9-dipath:
    visited nodes: set()
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    target (9) not found on 1->3. keep walking along this arc
    finding 3,9-dipath:
    visited nodes: {1}
    traversing cut [3]: {3->2, 3->10, 3->9}
    on arc 3->2
    target (9) not found on 3->2. keep walking along this arc
    finding 2,9-dipath:
    visited nodes: {1, 3}
    traversing cut [2]: {2->7, 2->4, 2->5}
    on arc 2->7
    target (9) not found on 2->7. keep walking along this arc
    finding 7,9-dipath:
    visited nodes: {1, 2, 3}
    traversing cut [7]: {7->5}
    on arc 7->5
    target (9) not found on 7->5. keep walking along this arc
    finding 5,9-dipath:
    visited nodes: {1, 2, 3, 7}
    traversing cut [5]: {5->9, 5->10}
    on arc 5->9
    target (9) found on 5->9
    adding 7->5 before [5->9]
    adding 2->7 before [7->5, 5->9]
    adding 3->2 before [2->7, 7->5, 5->9]
    adding 1->3 before [3->2, 2->7, 7->5, 5->9]
    find 19-dipath:  [1->3, 3->2, 2->7, 7->5, 5->9]
    """
    ### Sample Test 2
    """
    edited supergraph:  {2->7, 1->5, 5->10, 10->1, 2->5, 3->9, 7->5, 3->2, 3->10, 5->9, 1->3, 1->2, 2->4}
    finding 1,9-dipath:
    visited nodes: set()
    traversing cut [1]: {1->5, 1->2, 1->3}
    on arc 1->5
    target (9) not found on 1->5. keep walking along this arc
    finding 5,9-dipath:
    visited nodes: {1}
    traversing cut [5]: {5->10, 5->9}
    on arc 5->10
    target (9) not found on 5->10. keep walking along this arc
    finding 10,9-dipath:
    visited nodes: {1, 5}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (9) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    on arc 5->9
    target (9) found on 5->9
    adding 1->5 before [5->9]
    find 19-dipath:  [1->5, 5->9]
    """
    ### Sample Output for the worst case: Traversed all arcs in the graph.
    """
    |{381-546}, 165 rows|

    finding 1,8-dipath:
    visited nodes: set()
    traversing cut [1]: {1->5, 1->2, 1->3}
    on arc 1->5
    target (8) not found on 1->5. keep walking along this arc
    finding 5,8-dipath:
    visited nodes: {1}
    traversing cut [5]: {5->10, 5->9}
    on arc 5->10
    target (8) not found on 5->10. keep walking along this arc
    finding 10,8-dipath:
    visited nodes: {1, 5}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    on arc 5->9
    target (8) not found on 5->9. keep walking along this arc
    finding 9,8-dipath:
    visited nodes: {1, 5}
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    cut [1] arc 1->5 failed. next
    on arc 1->2
    target (8) not found on 1->2. keep walking along this arc
    finding 2,8-dipath:
    visited nodes: {1}
    traversing cut [2]: {2->7, 2->5, 2->4}
    on arc 2->7
    target (8) not found on 2->7. keep walking along this arc
    finding 7,8-dipath:
    visited nodes: {1, 2}
    traversing cut [7]: {7->5}
    on arc 7->5
    target (8) not found on 7->5. keep walking along this arc
    finding 5,8-dipath:
    visited nodes: {1, 2, 7}
    traversing cut [5]: {5->10, 5->9}
    on arc 5->10
    target (8) not found on 5->10. keep walking along this arc
    finding 10,8-dipath:
    visited nodes: {1, 2, 5, 7}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    on arc 5->9
    target (8) not found on 5->9. keep walking along this arc
    finding 9,8-dipath:
    visited nodes: {1, 2, 5, 7}
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    cut [7] arc 7->5 failed. next
    cut [2] arc 2->7 failed. next
    on arc 2->5
    target (8) not found on 2->5. keep walking along this arc
    finding 5,8-dipath:
    visited nodes: {1, 2}
    traversing cut [5]: {5->10, 5->9}
    on arc 5->10
    target (8) not found on 5->10. keep walking along this arc
    finding 10,8-dipath:
    visited nodes: {1, 2, 5}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    on arc 5->9
    target (8) not found on 5->9. keep walking along this arc
    finding 9,8-dipath:
    visited nodes: {1, 2, 5}
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    cut [2] arc 2->5 failed. next
    on arc 2->4
    target (8) not found on 2->4. keep walking along this arc
    finding 4,8-dipath:
    visited nodes: {1, 2}
    traversing cut [4]: set()
    cut [2] arc 2->4 failed. next
    cut [1] arc 1->2 failed. next
    on arc 1->3
    target (8) not found on 1->3. keep walking along this arc
    finding 3,8-dipath:
    visited nodes: {1}
    traversing cut [3]: {3->9, 3->2, 3->10}
    on arc 3->9
    target (8) not found on 3->9. keep walking along this arc
    finding 9,8-dipath:
    visited nodes: {1, 3}
    traversing cut [9]: set()
    cut [3] arc 3->9 failed. next
    on arc 3->2
    target (8) not found on 3->2. keep walking along this arc
    finding 2,8-dipath:
    visited nodes: {1, 3}
    traversing cut [2]: {2->7, 2->5, 2->4}
    on arc 2->7
    target (8) not found on 2->7. keep walking along this arc
    finding 7,8-dipath:
    visited nodes: {1, 2, 3}
    traversing cut [7]: {7->5}
    on arc 7->5
    target (8) not found on 7->5. keep walking along this arc
    finding 5,8-dipath:
    visited nodes: {1, 2, 3, 7}
    traversing cut [5]: {5->10, 5->9}
    on arc 5->10
    target (8) not found on 5->10. keep walking along this arc
    finding 10,8-dipath:
    visited nodes: {1, 2, 3, 5, 7}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    on arc 5->9
    target (8) not found on 5->9. keep walking along this arc
    finding 9,8-dipath:
    visited nodes: {1, 2, 3, 5, 7}
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    cut [7] arc 7->5 failed. next
    cut [2] arc 2->7 failed. next
    on arc 2->5
    target (8) not found on 2->5. keep walking along this arc
    finding 5,8-dipath:
    visited nodes: {1, 2, 3}
    traversing cut [5]: {5->10, 5->9}
    on arc 5->10
    target (8) not found on 5->10. keep walking along this arc
    finding 10,8-dipath:
    visited nodes: {1, 2, 3, 5}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    on arc 5->9
    target (8) not found on 5->9. keep walking along this arc
    finding 9,8-dipath:
    visited nodes: {1, 2, 3, 5}
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    cut [2] arc 2->5 failed. next
    on arc 2->4
    target (8) not found on 2->4. keep walking along this arc
    finding 4,8-dipath:
    visited nodes: {1, 2, 3}
    traversing cut [4]: set()
    cut [2] arc 2->4 failed. next
    cut [3] arc 3->2 failed. next
    on arc 3->10
    target (8) not found on 3->10. keep walking along this arc
    finding 10,8-dipath:
    visited nodes: {1, 3}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [3] arc 3->10 failed. next
    cut [1] arc 1->3 failed. next
    no 18-dipath:  False
    """

    ### version 2
    ### keeps tracking all nodes visited in all later procedures, and sending information back to preceeding 
    ### nodes to avoid reaching those nodes visited later.
    ### improvements: reduces duplicate nodes visited
    """
    def find_dipath(arcs, i, j, visited_nodes = None, process = False):
        assert i != j, "cannot use for dicycle"
        ### initialize set for each new call
        if visited_nodes is None:
            visited_nodes = set()
        i_cut = tail_arcs(i, arcs)
        visited_nodes.add(i)
        #visited_nodes.add(i)
        if process:
            print(f"finding {i},{j}-dipath:")
            print(f"visited nodes: {visited_nodes}")
            print(f"traversing cut [{i}]: {i_cut}")
        ### traverse the cut
        for arc in i_cut:
            if process:
                print(f"on arc {arc}")
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
                rest = find_dipath(arcs, arc.head(), j, visited_nodes, process)
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
    """
    ### tests version 2
    """
        dipath1:  {1->3, 5->6, 3->5}
        finding 1,6-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3}
        on arc 1->3
        target (6) not found on 1->3. keep walking along this arc
        finding 3,6-dipath:
        visited nodes: {1, 3}
        traversing cut [3]: {3->5}
        on arc 3->5
        target (6) not found on 3->5. keep walking along this arc
        finding 5,6-dipath:
        visited nodes: {1, 3, 5}
        traversing cut [5]: {5->6}
        on arc 5->6
        target (6) found on 5->6
        adding 3->5 before [5->6]
        adding 1->3 before [3->5, 5->6]
        find 16-dipath in dipath1:  [1->3, 3->5, 5->6]

        finding 3,5-dipath:
        visited nodes: {3}
        traversing cut [3]: {3->5}
        on arc 3->5
        target (5) found on 3->5
        find 35-dipath in dipath1:  [3->5]

        finding 3,6-dipath:
        visited nodes: {3}
        traversing cut [3]: {3->5}
        on arc 3->5
        target (6) not found on 3->5. keep walking along this arc
        finding 5,6-dipath:
        visited nodes: {3, 5}
        traversing cut [5]: {5->6}
        on arc 5->6
        target (6) found on 5->6
        adding 3->5 before [5->6]
        find 36-dipath in dipath1:  [3->5, 5->6]

        finding 4,5-dipath:
        visited nodes: {4}
        traversing cut [4]: set()
        no 45-dipath in dipath1:  False

        finding 2,4-dipath:
        visited nodes: {2}
        traversing cut [2]: set()
        no 24-dipath in dipath1:  False

        dipath2:  {1->3, 2->7, 1->5}
        finding 1,7-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3, 1->5}
        on arc 1->3
        target (7) not found on 1->3. keep walking along this arc
        finding 3,7-dipath:
        visited nodes: {1, 3}
        traversing cut [3]: set()
        cut [1] arc 1->3 failed. next
        on arc 1->5
        target (7) not found on 1->5. keep walking along this arc
        finding 5,7-dipath:
        visited nodes: {1, 3, 5}
        traversing cut [5]: set()
        cut [1] arc 1->5 failed. next
        no 17-dipath:  False

        finding 1,3-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3, 1->5}
        on arc 1->3
        target (3) found on 1->3
        find 13-dipath:  [1->3]

        finding 5,6-dipath:
        visited nodes: {5}
        traversing cut [5]: set()
        find 56-dipath:  False

        Supergraph:  {3->9, 2->5, 1->3, 5->10, 10->1, 1->2, 2->4, 1->5, 3->2, 3->10}
        finding 1,2-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3, 1->2, 1->5}
        on arc 1->3
        target (2) not found on 1->3. keep walking along this arc
        finding 3,2-dipath:
        visited nodes: {1, 3}
        traversing cut [3]: {3->2, 3->9, 3->10}
        on arc 3->2
        target (2) found on 3->2
        adding 1->3 before [3->2]
        find 12-dipath:  [1->3, 3->2]
        edited supergraph:  {7->5, 3->9, 2->7, 2->5, 1->3, 5->10, 10->1, 1->2, 5->9, 2->4, 1->5, 3->2, 3->10}
        finding 1,9-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3, 1->2, 1->5}
        on arc 1->3
        target (9) not found on 1->3. keep walking along this arc
        finding 3,9-dipath:
        visited nodes: {1, 3}
        traversing cut [3]: {3->2, 3->9, 3->10}
        on arc 3->2
        target (9) not found on 3->2. keep walking along this arc
        finding 2,9-dipath:
        visited nodes: {1, 2, 3}
        traversing cut [2]: {2->5, 2->7, 2->4}
        on arc 2->5
        target (9) not found on 2->5. keep walking along this arc
        finding 5,9-dipath:
        visited nodes: {1, 2, 3, 5}
        traversing cut [5]: {5->9, 5->10}
        on arc 5->9
        target (9) found on 5->9
        adding 2->5 before [5->9]
        adding 3->2 before [2->5, 5->9]
        adding 1->3 before [3->2, 2->5, 5->9]
        find 19-dipath:  [1->3, 3->2, 2->5, 5->9]

        |{720-783}, 63 rows|
        finding 1,8-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3, 1->2, 1->5}
        on arc 1->3
        target (8) not found on 1->3. keep walking along this arc
        finding 3,8-dipath:
        visited nodes: {1, 3}
        traversing cut [3]: {3->2, 3->9, 3->10}
        on arc 3->2
        target (8) not found on 3->2. keep walking along this arc
        finding 2,8-dipath:
        visited nodes: {1, 2, 3}
        traversing cut [2]: {2->5, 2->7, 2->4}
        on arc 2->5
        target (8) not found on 2->5. keep walking along this arc
        finding 5,8-dipath:
        visited nodes: {1, 2, 3, 5}
        traversing cut [5]: {5->9, 5->10}
        on arc 5->9
        target (8) not found on 5->9. keep walking along this arc
        finding 9,8-dipath:
        visited nodes: {1, 2, 3, 5, 9}
        traversing cut [9]: set()
        cut [5] arc 5->9 failed. next
        on arc 5->10
        target (8) not found on 5->10. keep walking along this arc
        finding 10,8-dipath:
        visited nodes: {1, 2, 3, 5, 9, 10}
        traversing cut [10]: {10->1}
        on arc 10->1
        target (8) not found on 10->1. keep walking along this arc
        head 1 is visited. skipping this arc.
        cut [5] arc 5->10 failed. next
        cut [2] arc 2->5 failed. next
        on arc 2->7
        target (8) not found on 2->7. keep walking along this arc
        finding 7,8-dipath:
        visited nodes: {1, 2, 3, 5, 7, 9, 10}
        traversing cut [7]: {7->5}
        on arc 7->5
        target (8) not found on 7->5. keep walking along this arc
        head 5 is visited. skipping this arc.
        cut [2] arc 2->7 failed. next
        on arc 2->4
        target (8) not found on 2->4. keep walking along this arc
        finding 4,8-dipath:
        visited nodes: {1, 2, 3, 4, 5, 7, 9, 10}
        traversing cut [4]: set()
        cut [2] arc 2->4 failed. next
        cut [3] arc 3->2 failed. next
        on arc 3->9
        target (8) not found on 3->9. keep walking along this arc
        head 9 is visited. skipping this arc.
        on arc 3->10
        target (8) not found on 3->10. keep walking along this arc
        head 10 is visited. skipping this arc.
        cut [1] arc 1->3 failed. next
        on arc 1->2
        target (8) not found on 1->2. keep walking along this arc
        head 2 is visited. skipping this arc.
        on arc 1->5
        target (8) not found on 1->5. keep walking along this arc
        head 5 is visited. skipping this arc.
        no 18-dipath:  False

        finding 1,4-dipath:
        visited nodes: {1}
        traversing cut [1]: {1->3, 1->2}
        on arc 1->3
        target (4) not found on 1->3. keep walking along this arc
        finding 3,4-dipath:
        visited nodes: {1, 3}
        traversing cut [3]: {3->4}
        on arc 3->4
        target (4) found on 3->4
        adding 1->3 before [3->4]


        14-dipath:  [1->3, 3->4]
    """

    ### advantages (from comparison of runtime of worst case, no 18-dipath): version 1 uses 165 rows, version 2 uses only 63 rows. WELL MORE EFFICIENT.

    ### version 3
    ### could avoid using some arcs, and track the length from starting node.
    """
    def find_dipath(arcs, i, j, visited_nodes = None, length = 0, avoid_arcs = None, process = False):
        assert i != j, "cannot use for dicycle"
        ### initialize set for each new call
        if visited_nodes is None:
            visited_nodes = set()
        i_cut = tail_arcs(i, arcs)
        visited_nodes.add(i)
        #visited_nodes.add(i)
        if process:
            print(f"finding {i},{j}-dipath:")
            print(f"visited nodes: {visited_nodes}")
            print(f"avoid using arcs: {avoid_arcs}")
            print(f"traversing cut [{i}]: {i_cut}")
        ### traverse the cut
        for arc in i_cut:
            if process:
                print(f"on arc {arc}")
            ### check if to avoid
            if not avoid_arcs is None:
                if arc in avoid_arcs:
                    if process:
                        print(f"avoid using {arc}")
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
                rest = find_dipath(arcs, arc.head(), j, visited_nodes, length + 1, avoid_arcs, process)
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
    """
    ### tests version 3
    print("\n\nTests for avoid_arcs: ")
    print("supergraph: ", supergraph)
    print("find 12-dipath without using arc 12: ", find_dipath(supergraph, 1, 2, avoid_arcs = {Arc(1, 2)}, process = True))
    print("find 12-dipath without using arcs 12, 13, 32: ", find_dipath(supergraph, 1, 2, avoid_arcs = {Arc(1, 2), Arc(1, 3), Arc(3, 2)}, process = True))
    print("all disjoint 12-dipath: ", all_disjoint_dipaths(supergraph, 1, 2))
    print_paths(all_disjoint_dipaths(supergraph, 1, 2))
    print("find 15-dipath without 12: ", find_dipath(supergraph, 1, 5, avoid_arcs = {Arc(1, 2)}, process = True))
    print("all disjoint 15-dipath: ", all_disjoint_dipaths(supergraph, 1, 5))
    print_paths(all_disjoint_dipaths(supergraph, 1, 5))

    """
    dipath1:  {1->3, 3->5, 5->6}
    finding 1,6-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3}
    on arc 1->3
    target (6) not found on 1->3. keep walking along this arc
    finding 3,6-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: None
    traversing cut [3]: {3->5}
    on arc 3->5
    target (6) not found on 3->5. keep walking along this arc
    finding 5,6-dipath:
    length from starting: 2
    visited nodes: {1, 3, 5}
    avoid using arcs: None
    traversing cut [5]: {5->6}
    on arc 5->6
    target (6) found on 5->6
    adding 3->5 before [5->6]
    adding 1->3 before [3->5, 5->6]
    find 16-dipath in dipath1:  [1->3, 3->5, 5->6]

    finding 3,5-dipath:
    length from starting: 0
    visited nodes: {3}
    avoid using arcs: None
    traversing cut [3]: {3->5}
    on arc 3->5
    target (5) found on 3->5
    find 35-dipath in dipath1:  [3->5]

    finding 3,6-dipath:
    length from starting: 0
    visited nodes: {3}
    avoid using arcs: None
    traversing cut [3]: {3->5}
    on arc 3->5
    target (6) not found on 3->5. keep walking along this arc
    finding 5,6-dipath:
    length from starting: 1
    visited nodes: {3, 5}
    avoid using arcs: None
    traversing cut [5]: {5->6}
    on arc 5->6
    target (6) found on 5->6
    adding 3->5 before [5->6]
    find 36-dipath in dipath1:  [3->5, 5->6]

    finding 4,5-dipath:
    length from starting: 0
    visited nodes: {4}
    avoid using arcs: None
    traversing cut [4]: set()
    no 45-dipath in dipath1:  False

    finding 2,4-dipath:
    length from starting: 0
    visited nodes: {2}
    avoid using arcs: None
    traversing cut [2]: set()
    no 24-dipath in dipath1:  False

    dipath2:  {1->3, 1->5, 2->7}
    finding 1,7-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->5}
    on arc 1->3
    target (7) not found on 1->3. keep walking along this arc
    finding 3,7-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: None
    traversing cut [3]: set()
    cut [1] arc 1->3 failed. next
    on arc 1->5
    target (7) not found on 1->5. keep walking along this arc
    finding 5,7-dipath:
    length from starting: 1
    visited nodes: {1, 3, 5}
    avoid using arcs: None
    traversing cut [5]: set()
    cut [1] arc 1->5 failed. next
    no 17-dipath:  False

    finding 1,3-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->5}
    on arc 1->3
    target (3) found on 1->3
    find 13-dipath:  [1->3]

    finding 5,6-dipath:
    length from starting: 0
    visited nodes: {5}
    avoid using arcs: None
    traversing cut [5]: set()
    find 56-dipath:  False

    Supergraph:  {5->10, 1->3, 2->4, 10->1, 3->10, 1->2, 1->5, 3->2, 3->9, 2->5}
    finding 1,2-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    target (2) not found on 1->3. keep walking along this arc
    finding 3,2-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: None
    traversing cut [3]: {3->2, 3->9, 3->10}
    on arc 3->2
    target (2) found on 3->2
    adding 1->3 before [3->2]
    find 12-dipath:  [1->3, 3->2]
    edited supergraph:  {5->9, 5->10, 1->3, 2->4, 10->1, 3->10, 1->2, 1->5, 3->2, 3->9, 2->7, 7->5, 2->5}
    finding 1,9-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    target (9) not found on 1->3. keep walking along this arc
    finding 3,9-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: None
    traversing cut [3]: {3->2, 3->9, 3->10}
    on arc 3->2
    target (9) not found on 3->2. keep walking along this arc
    finding 2,9-dipath:
    length from starting: 2
    visited nodes: {1, 2, 3}
    avoid using arcs: None
    traversing cut [2]: {2->4, 2->5, 2->7}
    on arc 2->4
    target (9) not found on 2->4. keep walking along this arc
    finding 4,9-dipath:
    length from starting: 3
    visited nodes: {1, 2, 3, 4}
    avoid using arcs: None
    traversing cut [4]: set()
    cut [2] arc 2->4 failed. next
    on arc 2->5
    target (9) not found on 2->5. keep walking along this arc
    finding 5,9-dipath:
    length from starting: 3
    visited nodes: {1, 2, 3, 4, 5}
    avoid using arcs: None
    traversing cut [5]: {5->9, 5->10}
    on arc 5->9
    target (9) found on 5->9
    adding 2->5 before [5->9]
    adding 3->2 before [2->5, 5->9]
    adding 1->3 before [3->2, 2->5, 5->9]
    find 19-dipath:  [1->3, 3->2, 2->5, 5->9]

    finding 1,8-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    target (8) not found on 1->3. keep walking along this arc
    finding 3,8-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: None
    traversing cut [3]: {3->2, 3->9, 3->10}
    on arc 3->2
    target (8) not found on 3->2. keep walking along this arc
    finding 2,8-dipath:
    length from starting: 2
    visited nodes: {1, 2, 3}
    avoid using arcs: None
    traversing cut [2]: {2->4, 2->5, 2->7}
    on arc 2->4
    target (8) not found on 2->4. keep walking along this arc
    finding 4,8-dipath:
    length from starting: 3
    visited nodes: {1, 2, 3, 4}
    avoid using arcs: None
    traversing cut [4]: set()
    cut [2] arc 2->4 failed. next
    on arc 2->5
    target (8) not found on 2->5. keep walking along this arc
    finding 5,8-dipath:
    length from starting: 3
    visited nodes: {1, 2, 3, 4, 5}
    avoid using arcs: None
    traversing cut [5]: {5->9, 5->10}
    on arc 5->9
    target (8) not found on 5->9. keep walking along this arc
    finding 9,8-dipath:
    length from starting: 4
    visited nodes: {1, 2, 3, 4, 5, 9}
    avoid using arcs: None
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    on arc 5->10
    target (8) not found on 5->10. keep walking along this arc
    finding 10,8-dipath:
    length from starting: 4
    visited nodes: {1, 2, 3, 4, 5, 9, 10}
    avoid using arcs: None
    traversing cut [10]: {10->1}
    on arc 10->1
    target (8) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    cut [2] arc 2->5 failed. next
    on arc 2->7
    target (8) not found on 2->7. keep walking along this arc
    finding 7,8-dipath:
    length from starting: 3
    visited nodes: {1, 2, 3, 4, 5, 7, 9, 10}
    avoid using arcs: None
    traversing cut [7]: {7->5}
    on arc 7->5
    target (8) not found on 7->5. keep walking along this arc
    head 5 is visited. skipping this arc.
    cut [2] arc 2->7 failed. next
    cut [3] arc 3->2 failed. next
    on arc 3->9
    target (8) not found on 3->9. keep walking along this arc
    head 9 is visited. skipping this arc.
    on arc 3->10
    target (8) not found on 3->10. keep walking along this arc
    head 10 is visited. skipping this arc.
    cut [1] arc 1->3 failed. next
    on arc 1->5
    target (8) not found on 1->5. keep walking along this arc
    head 5 is visited. skipping this arc.
    on arc 1->2
    target (8) not found on 1->2. keep walking along this arc
    head 2 is visited. skipping this arc.
    no 18-dipath:  False


    Tests for avoid_arcs: 
    supergraph:  {5->9, 5->10, 1->3, 2->4, 10->1, 3->10, 1->2, 1->5, 3->2, 3->9, 2->7, 7->5, 2->5}
    finding 1,2-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: {1->2}
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    target (2) not found on 1->3. keep walking along this arc
    finding 3,2-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: {1->2}
    traversing cut [3]: {3->2, 3->9, 3->10}
    on arc 3->2
    target (2) found on 3->2
    adding 1->3 before [3->2]
    find 12-dipath without using arc 12:  [1->3, 3->2]
    finding 1,2-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: {1->3, 3->2, 1->2}
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    avoid using 1->3
    on arc 1->5
    target (2) not found on 1->5. keep walking along this arc
    finding 5,2-dipath:
    length from starting: 1
    visited nodes: {1, 5}
    avoid using arcs: {1->3, 3->2, 1->2}
    traversing cut [5]: {5->9, 5->10}
    on arc 5->9
    target (2) not found on 5->9. keep walking along this arc
    finding 9,2-dipath:
    length from starting: 2
    visited nodes: {1, 5, 9}
    avoid using arcs: {1->3, 3->2, 1->2}
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    on arc 5->10
    target (2) not found on 5->10. keep walking along this arc
    finding 10,2-dipath:
    length from starting: 2
    visited nodes: {1, 10, 5, 9}
    avoid using arcs: {1->3, 3->2, 1->2}
    traversing cut [10]: {10->1}
    on arc 10->1
    target (2) not found on 10->1. keep walking along this arc
    head 1 is visited. skipping this arc.
    cut [5] arc 5->10 failed. next
    cut [1] arc 1->5 failed. next
    on arc 1->2
    avoid using 1->2
    find 12-dipath without using arcs 12, 13, 32:  False
    all disjoint 12-dipath:  [[1->3, 3->2], [1->2]]
    Found 2 paths in total:
    Path 1: [1->3, 3->2]
    Path 2: [1->2]
    finding 1,5-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: {1->2}
    traversing cut [1]: {1->3, 1->5, 1->2}
    on arc 1->3
    target (5) not found on 1->3. keep walking along this arc
    finding 3,5-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: {1->2}
    traversing cut [3]: {3->2, 3->9, 3->10}
    on arc 3->2
    target (5) not found on 3->2. keep walking along this arc
    finding 2,5-dipath:
    length from starting: 2
    visited nodes: {1, 2, 3}
    avoid using arcs: {1->2}
    traversing cut [2]: {2->4, 2->5, 2->7}
    on arc 2->4
    target (5) not found on 2->4. keep walking along this arc
    finding 4,5-dipath:
    length from starting: 3
    visited nodes: {1, 2, 3, 4}
    avoid using arcs: {1->2}
    traversing cut [4]: set()
    cut [2] arc 2->4 failed. next
    on arc 2->5
    target (5) found on 2->5
    adding 3->2 before [2->5]
    adding 1->3 before [3->2, 2->5]
    find 15-dipath without 12:  [1->3, 3->2, 2->5]
    all disjoint 15-dipath:  [[1->3, 3->2, 2->5], [1->5], [1->2, 2->7, 7->5]]
    Found 3 paths in total:
    Path 1: [1->3, 3->2, 2->5]
    Path 2: [1->5]
    Path 3: [1->2, 2->7, 7->5]
    """

    ### version 4
    """
    def find_dipath(arcs, i, j, visited_nodes = None, limit = None, length = 0, avoid_arcs = None, process = False):
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
            print(f"traversing cut [{i}]: {i_cut}")
        ### traverse the cut
        for arc in i_cut:
            if process:
                print(f"on arc {arc}")
            ### check if to avoid
            if not avoid_arcs is None:
                if arc in avoid_arcs:
                    if process:
                        print(f"avoid using {arc}")
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
                rest = find_dipath(arcs, arc.head(), j, visited_nodes, limit, length + 1, avoid_arcs, process)
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
    """

    ### tests length limit
    print("supergraph: ", supergraph)
    print("find 12-dipath in length 1: ", find_dipath(supergraph, 1, 2, limit = 1, process = True))
    print("find 12-dipath in length 2: ", find_dipath(supergraph, 1, 2, limit = 2, process = True))
    print("find 12-dipath in length 1 and avoid 12: ", find_dipath(supergraph, 1, 2, limit = 1, avoid_arcs = {Arc(1, 2)}, process = True))

    """
    supergraph:  {3->10, 3->2, 1->5, 1->2, 7->5, 5->10, 5->9, 1->3, 2->5, 3->9, 2->4, 2->7, 10->1}
    finding 1,2-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->2, 1->5}
    on arc 1->3
    target (2) not found on 1->3. keep walking along this arc
    exceed length limit
    cut [1] arc 1->3 failed. next
    on arc 1->2
    target (2) found on 1->2
    find 12-dipath in length 1:  [1->2]
    finding 1,2-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: None
    traversing cut [1]: {1->3, 1->2, 1->5}
    on arc 1->3
    target (2) not found on 1->3. keep walking along this arc
    finding 3,2-dipath:
    length from starting: 1
    visited nodes: {1, 3}
    avoid using arcs: None
    traversing cut [3]: {3->10, 3->2, 3->9}
    on arc 3->10
    target (2) not found on 3->10. keep walking along this arc
    exceed length limit
    cut [3] arc 3->10 failed. next
    on arc 3->2
    target (2) found on 3->2
    adding 1->3 before [3->2]
    find 12-dipath in length 2:  [1->3, 3->2]
    finding 1,2-dipath:
    length from starting: 0
    visited nodes: {1}
    avoid using arcs: {1->2}
    traversing cut [1]: {1->3, 1->2, 1->5}
    on arc 1->3
    target (2) not found on 1->3. keep walking along this arc
    exceed length limit
    cut [1] arc 1->3 failed. next
    on arc 1->2
    avoid using 1->2
    on arc 1->5
    target (2) not found on 1->5. keep walking along this arc
    exceed length limit
    cut [1] arc 1->5 failed. next
    find 12-dipath in length 1 and avoid 12:  False
    """

if TEST_FIND_PATH:
    graph1 = {Edge(1, 3), Edge(3, 4), Edge(4, 5)}
    print("graph1: ", graph1)
    print("find 15-path: ", find_path(graph1, 1, 5, process = True))

    graph2 = {Edge(1, 2), Edge(2, 3), Edge(3, 4), Edge(4, 5), Edge(5, 1)}
    print("graph2: ", graph2)
    print("find 15-path: ", find_path(graph2, 1, 5, process = True))
    print("no 17-path: ", find_path(graph2, 1, 7, process = True))



if TEST_FIND_DIPATH_FUNS:
    print("7 is reachable from 1: ", if_reachable(supergraph, 1, 7))
    print(find_dipath(supergraph, 1, 7))
    print("12 is not reachable from 1: ", find_dipath(supergraph, 1, 12))
    print(find_dipath(supergraph, 1, 12))
    print("all disjoint 19-dipath: ", all_disjoint_dipaths(supergraph, 1, 9, if_print = True))
    print("all disjoint 19-dipath in length 2: ", all_disjoint_dipaths(supergraph, 1, 9, limit = 2, if_print = True))
    print("dipath 1: ", dipath1)
    print("no dicycle containing 3: ", find_dicycle(dipath1, 3, process = True))

    ### sample output
    """
    7 is reachable from 1:  True
    [1->2, 2->7]
    12 is not reachable from 1:  False
    False
    Found 2 paths in total:
    Path 1: [1->2, 2->7, 7->5, 5->9]
    Path 2: [1->3, 3->9]
    all disjoint 19-dipath:  [[1->2, 2->7, 7->5, 5->9], [1->3, 3->9]]
    Found 2 paths in total:
    Path 1: [1->3, 3->9]
    Path 2: [1->5, 5->9]
    all disjoint 19-dipath in length 2:  [[1->3, 3->9], [1->5, 5->9]]
    """

if TEST_FIND_DICYCLE:
    print("supergraph: ", supergraph)
    print("dipath containing 1", find_dicycle(supergraph, 1, process = True))
    print("dicycle containing 2: ", find_dicycle(supergraph, 2, process = True))
    print("dicycle containing 3: ", find_dicycle(supergraph, 3))
    print("no dicycle containing 4: ", find_dicycle(supergraph, 4, process = True))

    ### sample output
    """
    supergraph:  {3->2, 7->5, 2->5, 2->7, 3->10, 5->9, 5->10, 3->9, 2->4, 1->5, 1->2, 1->3, 10->1}
    cut [1]: {1->5, 1->2, 1->3}
    on arc 1->5:
    finding 5,1-dipath:
    length from starting: 0
    visited nodes: {5}
    avoid using arcs: None
    traversing cut [5]: {5->9, 5->10}
    on arc 5->9
    target (1) not found on 5->9. keep walking along this arc
    finding 9,1-dipath:
    length from starting: 1
    visited nodes: {9, 5}
    avoid using arcs: None
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    on arc 5->10
    target (1) not found on 5->10. keep walking along this arc
    finding 10,1-dipath:
    length from starting: 1
    visited nodes: {9, 10, 5}
    avoid using arcs: None
    traversing cut [10]: {10->1}
    on arc 10->1
    target (1) found on 10->1
    adding 5->10 before [10->1]
    found 5,1-dipath. adding 1->5 before
    dipath containing 1 [1->5, 5->10, 10->1]
    cut [2]: {2->4, 2->5, 2->7}
    on arc 2->4:
    finding 4,2-dipath:
    length from starting: 0
    visited nodes: {4}
    avoid using arcs: None
    traversing cut [4]: set()
    no 4,2-dipath exists. skipping arc 2->4
    on arc 2->5:
    finding 5,2-dipath:
    length from starting: 0
    visited nodes: {5}
    avoid using arcs: None
    traversing cut [5]: {5->9, 5->10}
    on arc 5->9
    target (2) not found on 5->9. keep walking along this arc
    finding 9,2-dipath:
    length from starting: 1
    visited nodes: {9, 5}
    avoid using arcs: None
    traversing cut [9]: set()
    cut [5] arc 5->9 failed. next
    on arc 5->10
    target (2) not found on 5->10. keep walking along this arc
    finding 10,2-dipath:
    length from starting: 1
    visited nodes: {9, 10, 5}
    avoid using arcs: None
    traversing cut [10]: {10->1}
    on arc 10->1
    target (2) not found on 10->1. keep walking along this arc
    finding 1,2-dipath:
    length from starting: 2
    visited nodes: {9, 10, 5, 1}
    avoid using arcs: None
    traversing cut [1]: {1->5, 1->2, 1->3}
    on arc 1->5
    target (2) not found on 1->5. keep walking along this arc
    head 5 is visited. skipping this arc.
    on arc 1->2
    target (2) found on 1->2
    adding 10->1 before [1->2]
    adding 5->10 before [10->1, 1->2]
    found 5,2-dipath. adding 2->5 before
    dicycle containing 2:  [2->5, 5->10, 10->1, 1->2]
    dicycle containing 3:  [3->10, 10->1, 1->3]
    cut [4]: set()
    no dicycles containing 4
    no dicycle containing 4:  False
    """

if TEST_FIND_ALL_DIPATHS:
    print("supergraph: ", supergraph)
    """
    result = []
    print("finding all 19-dipaths: ")
    find_all_dipaths(supergraph, 1, 9, result = result)
    print_paths(result)
    """
    all_dipaths(supergraph, 1, 9, if_print = True)
    print()
    ### sample output
    """
    supergraph:  {2->4, 5->9, 1->2, 10->1, 5->10, 7->5, 1->5, 2->5, 3->9, 3->10, 3->2, 2->7, 1->3}
    finding 1,9-dipath:
    cut [1]: {1->5, 1->2, 1->3}
    current dipath: []
    visited nodes: [1]
    visited/found wanted dipaths: []
    length from start: 0
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 1->5
    target (9) is not found on 1->5. next
    finding 5,9-dipath:
    cut [5]: {5->9, 5->10}
    current dipath: [1->5]
    visited nodes: [1, 5]
    visited/found wanted dipaths: []
    length from start: 1
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 5->9
    found dipath ending (9). adding 5->9 after [1->5]
    >>>>>>>>>>>>> now on arc 5->10
    target (9) is not found on 5->10. next
    finding 10,9-dipath:
    cut [10]: {10->1}
    current dipath: [1->5, 5->10]
    visited nodes: [1, 5, 10]
    visited/found wanted dipaths: [[1->5, 5->9]]
    length from start: 2
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 10->1
    target (9) is not found on 10->1. next
    1 is visited. skipping this arc 10->1
    >>>>>>>>>>>>> now on arc 1->2
    target (9) is not found on 1->2. next
    finding 2,9-dipath:
    cut [2]: {2->4, 2->7, 2->5}
    current dipath: [1->2]
    visited nodes: [1, 2]
    visited/found wanted dipaths: [[1->5, 5->9]]
    length from start: 1
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 2->4
    target (9) is not found on 2->4. next
    finding 4,9-dipath:
    cut [4]: set()
    current dipath: [1->2, 2->4]
    visited nodes: [1, 2, 4]
    visited/found wanted dipaths: [[1->5, 5->9]]
    length from start: 2
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 2->7
    target (9) is not found on 2->7. next
    finding 7,9-dipath:
    cut [7]: {7->5}
    current dipath: [1->2, 2->7]
    visited nodes: [1, 2, 7]
    visited/found wanted dipaths: [[1->5, 5->9]]
    length from start: 2
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 7->5
    target (9) is not found on 7->5. next
    finding 5,9-dipath:
    cut [5]: {5->9, 5->10}
    current dipath: [1->2, 2->7, 7->5]
    visited nodes: [1, 2, 7, 5]
    visited/found wanted dipaths: [[1->5, 5->9]]
    length from start: 3
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 5->9
    found dipath ending (9). adding 5->9 after [1->2, 2->7, 7->5]
    >>>>>>>>>>>>> now on arc 5->10
    target (9) is not found on 5->10. next
    finding 10,9-dipath:
    cut [10]: {10->1}
    current dipath: [1->2, 2->7, 7->5, 5->10]
    visited nodes: [1, 2, 7, 5, 10]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9]]
    length from start: 4
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 10->1
    target (9) is not found on 10->1. next
    1 is visited. skipping this arc 10->1
    >>>>>>>>>>>>> now on arc 2->5
    target (9) is not found on 2->5. next
    finding 5,9-dipath:
    cut [5]: {5->9, 5->10}
    current dipath: [1->2, 2->5]
    visited nodes: [1, 2, 5]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9]]
    length from start: 2
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 5->9
    found dipath ending (9). adding 5->9 after [1->2, 2->5]
    >>>>>>>>>>>>> now on arc 5->10
    target (9) is not found on 5->10. next
    finding 10,9-dipath:
    cut [10]: {10->1}
    current dipath: [1->2, 2->5, 5->10]
    visited nodes: [1, 2, 5, 10]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9]]
    length from start: 3
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 10->1
    target (9) is not found on 10->1. next
    1 is visited. skipping this arc 10->1
    >>>>>>>>>>>>> now on arc 1->3
    target (9) is not found on 1->3. next
    finding 3,9-dipath:
    cut [3]: {3->2, 3->9, 3->10}
    current dipath: [1->3]
    visited nodes: [1, 3]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9]]
    length from start: 1
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 3->2
    target (9) is not found on 3->2. next
    finding 2,9-dipath:
    cut [2]: {2->4, 2->7, 2->5}
    current dipath: [1->3, 3->2]
    visited nodes: [1, 3, 2]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9]]
    length from start: 2
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 2->4
    target (9) is not found on 2->4. next
    finding 4,9-dipath:
    cut [4]: set()
    current dipath: [1->3, 3->2, 2->4]
    visited nodes: [1, 3, 2, 4]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9]]
    length from start: 3
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 2->7
    target (9) is not found on 2->7. next
    finding 7,9-dipath:
    cut [7]: {7->5}
    current dipath: [1->3, 3->2, 2->7]
    visited nodes: [1, 3, 2, 7]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9]]
    length from start: 3
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 7->5
    target (9) is not found on 7->5. next
    finding 5,9-dipath:
    cut [5]: {5->9, 5->10}
    current dipath: [1->3, 3->2, 2->7, 7->5]
    visited nodes: [1, 3, 2, 7, 5]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9]]
    length from start: 4
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 5->9
    found dipath ending (9). adding 5->9 after [1->3, 3->2, 2->7, 7->5]
    >>>>>>>>>>>>> now on arc 5->10
    target (9) is not found on 5->10. next
    finding 10,9-dipath:
    cut [10]: {10->1}
    current dipath: [1->3, 3->2, 2->7, 7->5, 5->10]
    visited nodes: [1, 3, 2, 7, 5, 10]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9], [1->3, 3->2, 2->7, 7->5, 5->9]]
    length from start: 5
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 10->1
    target (9) is not found on 10->1. next
    1 is visited. skipping this arc 10->1
    >>>>>>>>>>>>> now on arc 2->5
    target (9) is not found on 2->5. next
    finding 5,9-dipath:
    cut [5]: {5->9, 5->10}
    current dipath: [1->3, 3->2, 2->5]
    visited nodes: [1, 3, 2, 5]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9], [1->3, 3->2, 2->7, 7->5, 5->9]]
    length from start: 3
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 5->9
    found dipath ending (9). adding 5->9 after [1->3, 3->2, 2->5]
    >>>>>>>>>>>>> now on arc 5->10
    target (9) is not found on 5->10. next
    finding 10,9-dipath:
    cut [10]: {10->1}
    current dipath: [1->3, 3->2, 2->5, 5->10]
    visited nodes: [1, 3, 2, 5, 10]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9], [1->3, 3->2, 2->7, 7->5, 5->9], [1->3, 3->2, 2->5, 5->9]]
    length from start: 4
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 10->1
    target (9) is not found on 10->1. next
    1 is visited. skipping this arc 10->1
    >>>>>>>>>>>>> now on arc 3->9
    found dipath ending (9). adding 3->9 after [1->3]
    >>>>>>>>>>>>> now on arc 3->10
    target (9) is not found on 3->10. next
    finding 10,9-dipath:
    cut [10]: {10->1}
    current dipath: [1->3, 3->10]
    visited nodes: [1, 3, 10]
    visited/found wanted dipaths: [[1->5, 5->9], [1->2, 2->7, 7->5, 5->9], [1->2, 2->5, 5->9], [1->3, 3->2, 2->7, 7->5, 5->9], [1->3, 3->2, 2->5, 5->9], [1->3, 3->9]]
    length from start: 2
    avoid arcs: None
    avoid nodes: None
    >>>>>>>>>>>>> now on arc 10->1
    target (9) is not found on 10->1. next
    1 is visited. skipping this arc 10->1
    finding 1,9-dipath:
    length limit: None
    avoid arcs: None
    avoid nodes: None
    Found 6 paths in total:
    Path 1: [1->5, 5->9]
    Path 2: [1->2, 2->7, 7->5, 5->9]
    Path 3: [1->2, 2->5, 5->9]
    Path 4: [1->3, 3->2, 2->7, 7->5, 5->9]
    Path 5: [1->3, 3->2, 2->5, 5->9]
    Path 6: [1->3, 3->9]
    """
    all_dipaths(supergraph, 1, 9, limit = 2, if_print = True)
    print()
    all_dipaths(supergraph, 1, 9, limit = 1, if_print = True)
    print()
    all_dipaths(supergraph, 1, 9, limit = 4, if_print = True)
    print()
    all_dipaths(supergraph, 2, 3, if_print = True)
    print()
    all_dipaths(supergraph, 3, 2, if_print = True)
    print()
    all_dicycles(supergraph, 1, if_print = True)
    print()
    all_dipaths(dipath1, 1, 3, if_print = True)
    print()
    all_dipaths(supergraph, 1, 4, if_print = True)
    print()
    all_dipaths(supergraph, 1, 4, avoid_arcs = {Arc(1, 2)}, if_print = True)
    all_dipaths(supergraph, 1, 4, avoid_arcs = {Arc(1, 2), Arc(1, 3)}, if_print = True)