# Atomic Selfish Routing Game based on Graphs.py
import Graphs as graph
import itertools as it
import functools as ft

class ARG:
    '''
    Assuming all players have the same source-target pair.
    traffics: tuple of traffic value for each player

    '''
    def __init__(self, NumPlayers, traffics, arcs, costs, source, target):
        assert NumPlayers >= 2, "At least two players are required."
        assert len(traffics) == NumPlayers, "Traffic list length mismatch."
        assert arcs == costs.keys(), "Arcs and Costs mismatch."

        self.NumPlayers = NumPlayers
        self.traffics = traffics
        self.graph = arcs
        self.costs = costs
        self.source = source
        self.target = target
        self.paths = tuple(sorted(graph.all_dipaths(self.graph, source, target), key=ft.cmp_to_key(graph.path_compare)))
        self.profiles = tuple(it.product(range(len(self.paths)), repeat=self.NumPlayers))
        self.flows = {profile:self._profile_to_flow(profile) for profile in self.profiles}
        self.flow_costs = {profile:self._profile_to_costs(profile) for profile in self.profiles}
        self.player_costs = {profile:self._profile_player_costs(profile, self.flow_costs[profile]) for profile in self.profiles}
        self.total_cost = {profile:self._total_cost(self.flows[profile], self.flow_costs[profile]) for profile in self.profiles}
        self.opt_cost, self.opt_flows = self._opt_flow()

    def _arcs_info(self, arcs_info):
        '''
        Print information on each arc (flow or cost).

        '''
        for arc in arcs_info:
            print(f"{arc}: {arcs_info[arc]}")

    def summary(self):
        '''
        Print a summary of this ARG.

        '''
        print_graph = sorted(list(self.graph))
        print("vvv=====================================================vvv")
        print(f"Atomic Selfish Routing Game with {self.NumPlayers} players:")
        print("------------------------------------")
        print(">>>Game:")
        print(print_graph)
        print("------------------------------------")
        self.print_paths()
        print("------------------------------------")
        print(f">>>Source: {self.source}, Target: {self.target}")
        print("------------------------------------")
        print(">>>Traffics for each player:")
        for idx in range(self.NumPlayers):
            print(f"Player {idx}: {self.traffics[idx]}")
        print("------------------------------------")
        print(f">>>Optimal social cost: {self.opt_cost}")
        print(">>>Optimal strategy profiles:")
        for profile in self.opt_flows:
            print(profile)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Flows and costs of all strategy profiles:")
        for profile in self.profiles:
            print("------------------------------------")
            print(f">>>Profile {profile} (Social cost: {self.total_cost[profile]}):")
            print("Arc: (Flow, Cost)")
            for arc in print_graph:
                print(f"{arc}: ({self.flows[profile][arc]}, {self.flow_costs[profile][arc]})")
            print(">>>Player costs:")
            for player in range(self.NumPlayers):
                print(f"Player {player}: {self.player_costs[profile][player]}")
        print("^^^=====================================================^^^")

    def print_paths(self):
        '''
        Print all available paths.
        
        '''
        print(">>>Avaiable paths:")
        for idx in range(len(self.paths)):
            print(f"Path {idx}: {self.paths[idx]}")

    def print_profiles(self):
        '''
        Print all avaiable strategy profiles.

        '''
        print(">>>Avaiable profiles:")
        for profile in self.profiles:
            print(profile)
    
    def print_profiles_flows(self):
        '''
        Print flows for all profiles.
        
        '''
        print(">>>Flows for all profiles:")
        for profile in self.profiles:
            print(f"{profile}:")
            self._arcs_info(self.flows[profile])

    def print_profiles_costs(self):
        '''
        Print costs for all profiles.

        '''
        print(">>>Costs for all profiles:")
        for profile in self.profiles:
            print(f"{profile}:")
            self._arcs_info(self.flow_costs[profile])

    def print_profiles_total_costs(self):
        '''
        Print total social costs for all profiles.

        '''
        print(">>>Total social costs for all profiles:")
        for profile in self.profiles:
            print(f"{profile}:")
            self._arcs_info(self.total_cost[profile])

    
    def _add_path_flow(self, flow, path, traffic):
        '''
        Add traffic amount to the path in the flow
        '''
        for arc in path:
            flow[arc] += traffic

    def _profile_to_flow(self, profile):
        '''
        Convert a profile to flow on each arc.

        '''
        # initialize flow to zero
        flow = {arc:0 for arc in self.graph}

        # add each player's traffic based on their chosen path
        for player in range(self.NumPlayers):
            self._add_path_flow(flow, self.paths[profile[player]], self.traffics[player])

        return flow
    
    def _flow_to_costs(self, flow):
        '''
        Convert a flow to cost on each arc.

        '''
        costs = {}
        for arc in flow:
            costs[arc] = self.costs[arc](flow[arc])

        return costs
    
    def _profile_to_costs(self, profile):
        '''
        Convert a profile to costs on each arc.

        '''
        return self._flow_to_costs(self._profile_to_flow(profile))
    
    def _path_cost(self, path, costs):
        '''
        Compute the total cost of a path. Each cost of arc appears once in the path.

        '''
        total = 0
        for arc in path:
            total += costs[arc]
        return total

    def _profile_player_costs(self, profile, costs):
        '''
        Compute each player's cost in a profile.

        '''
        player_costs = []
        for idx in range(self.NumPlayers):
            player_costs.append(self._path_cost(self.paths[profile[idx]], costs))
        return tuple(player_costs)

    def _total_cost(self, flow, costs):
        '''
        Compute the total social cost of the flow.

        '''
        total = 0
        for arc in flow:
            total += flow[arc] * costs[arc]
        return total
    
    def _opt_flow(self):
        '''
        Compute the optimal flow
        
        '''
        min_cost = min(self.total_cost.values())
        opt_profiles = [profile for profile in self.profiles if self.total_cost[profile] == min_cost]
        return min_cost, tuple(opt_profiles)
            

# sample uses
if __name__ == "__main__":
    #Goemans, Mirrokni, Vetta atomic selfish routing instance
    GMV = {graph.Arc('s','w'),graph.Arc('s','v'),graph.Arc('s','t'),graph.Arc('v','w'),graph.Arc('v','t'),graph.Arc('w','t')}
    #print(GMV)

    #self.paths=tuple([[graph.Arc('s','t')],[graph.Arc('s','w'),graph.Arc('w','t')],[graph.Arc('s','v'),graph.Arc('v','t')],[graph.Arc('s','v'),graph.Arc('v','w'),graph.Arc('w','t')]])
    
    paths = graph.all_dipaths(GMV, 's', 't')
    #print(tuple(paths))

    #print(list(it.permutations(range(len(paths)), 2)))

    def Csw(x):
        return x+33
    
    def Csv(x):
        return 3 * x**2
    
    def Cst(x):
        return 47 * x
    
    def Cvw(x):
        return 6 * x**2
    
    def Cvt(x):
        return x**2 + 44
    
    def Cwt(x):
        return 13 * x

    costs = {graph.Arc('s','w'):Csw,graph.Arc('s','v'):Csv,graph.Arc('s','t'):Cst,graph.Arc('v','w'):Cvw,graph.Arc('v','t'):Cvt,graph.Arc('w','t'):Cwt}
    game = ARG(2, (1,1), GMV, costs, 's', 't')
    game.summary()

    game2 = ARG(2, (1,2), GMV, costs, 's', 't')
    game2.summary()

    game3 = ARG(4, (1,10,9,3), GMV, costs, 's', 't')
    game3.summary()
