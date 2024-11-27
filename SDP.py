### Shortest Dipath Problem
### involves lots of useful functions for finding the shortest dipath.
from Graphs import *
from TP_data_struct import *
### For shortest dipath problem, we ignore the constraints, just costs.
### Nodes are labeled from s, ..., t, s=1 and t=n, the numerical index of the last node.
### Node Demands: bv= -(|N|-1) if v=s or 1 otherwise.
### TRS: Tree rooted from s: a TREE such that all nodes other than s are reachable from s.
### STRS: Shortest tree rooted from s: a TRS such that any (unique) sv-dipath in the TRS is shortest among the whole graph.
### LTRS: Longest tree rooted from from s.


__TEST_BASIC = False
__TEST_DIJKSTRA = False
__TEST_SDP = False



def cost_dipath(dipath, costs):
    """
    finds the cost of the given dipath.
    cost_dipath: Dipath Costs -> Float

    """
    result = 0
    for arc in dipath:
        result += costs[arc]
    return result

def all_dipath_costs(dipaths, costs):
    """
    returns a dictionary with cost of every dipath in dipaths

    """
    return {tuple(dipath): cost_dipath(dipath, costs) for dipath in dipaths}

def shortest_dipath(arcs, costs, i, j):
    """
    brute force to find all shortest ij-dipaths (not recommended for use)
    will return a tuple, (min dipath, min cost)
    
    """
    #result = {tuple(dipath): cost_dipath(dipath, costs) for dipath in all_dipaths(arcs, i, j)}
    dipaths = all_dipaths(arcs, i, j)

    #result = {tuple(dipath): cost_dipath(dipath, costs) for dipath in dipaths} // can be replaced
    result = all_dipath_costs(dipaths, costs)

    #result = min(filter(lambda x: cost_dipath(x, costs), all_dipaths(arcs, i, j)))
    #shortest = min(result, key=result.get)
    shortest = min(result.values())
    #return list(filter(lambda x: result.get(x) == shortest, result))
    return [dipath for dipath in dipaths if result[tuple(dipath)] == shortest], shortest

def longest_dipath(arcs, costs, i, j):
    """
    same logic as shortest_dipath.
    
    """
    dipaths = all_dipaths(arcs, i, j)
    #result = {tuple(dipath): cost_dipath(dipath, costs) for dipath in dipaths}
    result = all_dipath_costs(dipaths, costs)
    longest = max(result.values())
    return [dipath for dipath in dipaths if result[tuple(dipath)] == longest], longest

cities = {Arc(1, 2), Arc(1, 3), Arc(1, 5), Arc(2, 3), Arc(3, 7), Arc(5, 2), Arc(5, 7), Arc(7, 1)}
city_costs = {Arc(1, 2): 1, Arc(1, 3): 3, Arc(1, 5): 2, Arc(2, 3): 9, Arc(3, 7): 1, Arc(5, 2): 3, Arc(5, 7):1, Arc(7, 1):3}

if __TEST_BASIC:
    ways12 = all_dipaths(cities, 1, 2)
    print("all 12-dipaths: ", ways12)
    ways17 = all_dipaths(cities, 1, 7)
    print("all 17-dipaths: ", ways17)
    print("12-dipaths costs: ", {tuple(dipath): cost_dipath(dipath, city_costs) for dipath in ways12})
    print("shortest 12-dipaths (by brute force): ", shortest_dipath(cities, city_costs, 1, 2))
    print("longest 12-dipath (by brute force): ", longest_dipath(cities, city_costs, 1, 2))


"""
Dijkstra's Algorithm:
INPUT: a graph where all nodes are reachable from s (or can only generate STRS with reachable nodes). costs are non-negative.
OUTPUT: a STRS. could find a shortest ij-dipath in the graph by using the unique ij-path in the tree.
Algorithm:
Step 0: Start with smallest st-cut, delta(S), where S={s}.
Step 1: Pick a shortest arc from the cut to be added into the output tree T, and the arc's head to be added to S.
Repeat Step 1 until all reachable nodes are involved in T. At termination, T is a STRS.

"""

def dijkstra(arcs, nodes, costs, start = 0, longest = False, if_print = False):
    """
    dijkstra's algorithm for finding the shortest dipath (shortest tree rooted from s).
    the cut is st-cut based on S, the visited nodes which always involve 1, namely the source node s. The final output should be tree.
    Will also give the Potens, which is the distance from s at that node.
    The start is the initial potential value for node s.

    """
    S = {1}
    T = set()
    Potens = {1: start}
    # namely S == nodes
    while len(S) != len(nodes):
        scut = dicut(S, arcs)
        shortest = None
        if longest:
            shortest = max(scut, key = costs.get)
        else:
            shortest = min(scut, key = costs.get)
        T.add(shortest)
        S.add(shortest.head())
        Potens[shortest.head()] = Potens[shortest.tail()] + costs[shortest]
    if if_print:
        print(f"Shortest Tree Found: {T}")
        print(f"Corresponding Distances: {Potens}")
    return T, Potens

if __TEST_DIJKSTRA:
    print("all 17-dipaths costs: ", all_dipath_costs(ways17, city_costs))
    shortest_cities = dijkstra(cities, arcs_to_nodes(cities), city_costs, if_print = True)
    print("shortest tree rooted from 1 in cities, ", shortest_cities)
    print("This is a tree: ", if_tree(shortest_cities[0], arcs_to_nodes(shortest_cities[0])))
    print("Cities is not a tree: ", if_tree(cities, arcs_to_nodes(cities)))
    shortest17 = all_dipaths(shortest_cities[0], 1, 7) ### should be only one
    print("should be only one 17-dipath from the tree, ", shortest17)
    print("shortest 17-dipath from the tree generated, ", shortest17[0], cost_dipath(shortest17[0], city_costs))
    print("all 17-dipaths costs:", dict_vertical(all_dipath_costs(all_dipaths(cities, 1, 7), city_costs)))

### sample output
"""
all 12-dipaths:  [[1->5, 5->2], [1->2]]
all 17-dipaths:  [[1->3, 3->7], [1->5, 5->2, 2->3, 3->7], [1->5, 5->7], [1->2, 2->3, 3->7]]
12-dipaths costs:  {(1->5, 5->2): 5, (1->2,): 1}
shortest 12-dipaths (by brute force):  ([[1->2]], 1)
longest 12-dipath (by brute force):  ([[1->5, 5->2]], 5)
all 17-dipaths costs:  {(1->3, 3->7): 4, (1->5, 5->2, 2->3, 3->7): 15, (1->5, 5->7): 3, (1->2, 2->3, 3->7): 11}
Shortest Tree Found: {1->3, 1->5, 1->2, 5->7}
Corresponding Distances: {1: 0, 2: 1, 5: 2, 7: 3, 3: 3}
shortest tree rooted from 1 in cities,  ({1->3, 1->5, 1->2, 5->7}, {1: 0, 2: 1, 5: 2, 7: 3, 3: 3})
This is a tree:  True
Cities is not a tree:  False
should be only one 17-dipath from the tree,  [[1->5, 5->7]]
shortest 17-dipath from the tree generated,  [1->5, 5->7] 3
all 17-dipaths costs: {(1->3, 3->7): 4}
{(1->5, 5->2, 2->3, 3->7): 15}
{(1->5, 5->7): 3}
{(1->2, 2->3, 3->7): 11}
"""



class SDP:
    """
    The Shortest Dipath Problem, G = (N, A, w, x).
    
    """
    def __init__(self, name: str, arcs, nodes, costs):
        """
        SDP(arcs, nodes, costs) creates a new SDP.
        Fields: __name (Str), __arcs (setof Arc), __nodes (setof Node), __costs (Dictof (Arc, Float)), __spotens (Dictof (Node, Float)),
                __lpotens (Dictof (Node, Float)), __strs (STRS), __ltrs (LTRS)

        """
        self.__name = name
        self.__arcs = arcs
        self.__nodes = nodes
        self.__costs = costs
        self.__spotens = None
        self.__lpotens = None
        self.__strs = None
        self.__ltrs = None

    def __repr__(self):
        return ">>>>>>>SDP-[" + self.__name + "]\n" + "Arcs:\n" + str(self.__arcs) + "\n" + "Nodes:\n" + str(self.__nodes) + "\n" + "Costs:\n" + str(self.__costs) \
                + "\n" + "Shortest Tree:\n" + str(self.__strs) + "\n" + "Shortest Distances:\n" + str(self.__spotens) + "\n" + "Longest Tree:\n" + str(self.__ltrs) \
                + "\n" + "Longest Distances:\n" + str(self.__lpotens)

    def optimize(self):
        """
        Perform algorithm to update shortest&longest trees.

        """
        shortest = dijkstra(self.__arcs, self.__nodes, self.__costs)
        longest = dijkstra(self.__arcs, self.__nodes, self.__costs, longest = True)
        self.__strs = shortest[0]
        self.__spotens = shortest[1]
        self.__ltrs = longest[0]
        self.__lpotens = longest[1]

if __TEST_SDP:
    SDP_cities = SDP("Cities", cities, arcs_to_nodes(cities), city_costs)
    print(SDP_cities)
    SDP_cities.optimize()
    print(SDP_cities)