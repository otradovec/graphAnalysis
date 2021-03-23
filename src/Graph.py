try:
    from Connection import Connection
except Exception as ignore:
    import src.Connection
try:
    from .Connection import Connection
except Exception as e:
    pass
import copy

class Graph:

    def __init__(self,nodes):
        self.nodes = nodes
        self.connections = []

    def has_node(self,nodeName):
        return nodeName in self.nodes

    def add_connection(self,first_node, second_node,oriented,value=1):
        self._add_connection(Connection(first_node,second_node,oriented,value))

    def _add_connection(self,connection):
        if not self.has_node(connection.begg) or not self.has_node(connection.to):
            raise ValueError("Adding connection with not existing node")
        self.connections.append(connection)

    def add_oriented_connection(self,first_node, second_node,value=1):
        self.add_connection(first_node,second_node,True,value)

    def add_oriented_connections(self,connections):
        for connection in connections:
            self.add_oriented_connection(connection[0],connection[1])

    def add_not_oriented_connection(self,first_node, second_node,value=1):
        self.add_connection(first_node,second_node,False,value)

    def add_not_oriented_connections(self,connections):
        for connection in connections:
            if len(connection) > 2:
                raise ValueError("Adding connection with too many arguments")
            self.add_not_oriented_connection(connection[0],connection[1])

    def add_not_oriented_valued_connections(self,connections):
        for connection in connections:
            if len(connection) > 3:
                raise ValueError("Adding connection with too many arguments")
            self.add_not_oriented_connection(connection[0],connection[1],connection[2])

    def is_connection(self,from_node, to_node):
        for conn in self.connections:
            if ((conn.begg == from_node) and (conn.to == to_node)):
                return True
            elif not conn.oriented and (conn.to == from_node and conn.begg == to_node):
                return True
        return False

    @staticmethod
    def __same_start_and_end(connectionA, connectionB):
        if isinstance(connectionA,Connection):
            return connectionA.begg == connectionB.begg and connectionA.to == connectionB.to
        else:
            return connectionA[0] == connectionB[0] and connectionA[1] == connectionB[1]

    def is_multigraph(self):
        if len(self.connections) < 2:
            return False
        multi = False
        for i in range(0,len(self.connections)):
            for j in range(i+1,len(self.connections)):
                if self.__same_start_and_end(self.connections[i],self.connections[j]):
                    multi = True
        return multi

    def is_oriented(self):
        return not self.is_bidirectional()

    def is_tree(self):
        if self.is_oriented():
            return False
        elif len(self.nodes) != (len(self.connections) + 1):
            return False
        else:
            return self.is_connected()

    def is_connected(self):
        if len(self.nodes) < 2:
            return True
        else:
            some_node = next(iter(self.nodes))
            return self.__reachable_nodes(some_node) == set(self.nodes)

    def has_loop(self):
        ret = False
        for connection in self.connections:
            if connection.begg == connection.to:
                ret = True
        return ret

    def __reachable_nodes(self,node):
        processed_nodes = set()
        unprocessed_nodes = set()
        unprocessed_nodes.add(node)
        while len(unprocessed_nodes) > 0:
            working_node = unprocessed_nodes.pop()
            processed_nodes.add(working_node)
            unprocessed_nodes.update(self.get_neighbors(working_node) - processed_nodes)
        return processed_nodes

    def has_connectivity(self):
        has = True
        for node in self.nodes:
            if len(self.__reachable_nodes(node)) < len(self.nodes):
                has = False
        return has

    def is_complete(self):
        comp = True
        import itertools
        for conn in itertools.product(["A","B","C","D","E","F"],repeat=2):
            if conn[0] != conn[1]:
                conn = list(conn)
                if not self.is_connection(conn[0],conn[1]):
                    comp = False
        return comp

    def has_bidirectional_edge(self):
        size = len(self.connections)
        if size > 1:
            for i in range(0,size-1):
                connectionA = self.connections[i]
                for j in range(i,size):
                    connectionB = self.connections[j]
                    if self.__are_opposite_direction(connectionA,connectionB):
                        return True
        return False

    def is_bidirectional(self):
        for conn in self.connections:
            if (not self.__has_edge_in_opposite_direction(conn)) and conn.oriented:
                return False
        return True

    def __has_edge_in_opposite_direction(self,conn):
        for opposite in self.connections:
            if self.__are_opposite_direction(conn,opposite):
                return True
        return False

    @staticmethod
    def __are_opposite_direction(connectionA,connectionB):
        if isinstance(connectionA,Connection):
            return connectionA.begg == connectionB.to and connectionA.to == connectionB.begg
        else:
            return connectionA[0] == connectionB[1] and connectionA[1] == connectionB[0]

    def get_leaving_edges_size(self,node):
        leaving_edges_size = 0
        for connection in self.connections:
            if (connection.begg == node) or (connection.to == node and not connection.oriented):
                    leaving_edges_size += 1
        return leaving_edges_size

    def __get_incoming_degree(self,node):
        incoming_degree = 0
        for connection in self.connections:
            if (connection.to == node) or (connection.begg == node and not connection.oriented):
                incoming_degree += 1
        return incoming_degree

    def total_cost(self):
        sum = 0
        for conn in self.connections:
            sum += int(conn.value)
        return sum

    def bridges(self):
        br = []
        for connection in self.connections:
            if self._is_bridge(connection):
                br.append(connection)
        return br

    def _is_bridge(self,connection):
        g = copy.deepcopy(self)
        before = len(g._components())
        g.remove_connection(connection)
        after = len(g._components())
        return before != after

    def separating_set(self):
        sep = set()
        for node in self.nodes:
            if self.is_separating(node):
                sep.add(node)
        return sep

    def is_separating(self,node):
        g = copy.deepcopy(self)
        before = len(g._components())
        g.remove_node(node)
        after = len(g._components())
        return before != after

    def remove_node(self,node):
        for connection in self.connections:
            if connection.begg == node or connection.to == node:
                self.remove_connection(connection)
        self.nodes.remove(node)

    def all_nodes_have_equal_in_out_degree(self):
        for node in self.nodes:
            if self.__get_incoming_degree(node) != self.get_leaving_edges_size(node):
                return False
        return True

    def get_degree(self,node):
        return self.get_leaving_edges_size(node) + self.__get_incoming_degree(node)

    def get_node_with_highest_degree(self):
        node_with_highest_degree = ("",-1)
        for node in self.nodes:
            degree = self.get_degree(node)
            if degree > node_with_highest_degree[1]:
                node_with_highest_degree = (node,degree)
        return node_with_highest_degree[0]

    def get_neighbors(self,node):
        neighbors = set()
        for connection in self.connections:
            if connection.begg == node:
                neighbors.add(connection.to)
            elif connection.to == node and not connection.oriented:
                neighbors.add(connection.begg)
        return neighbors


    def get_minimal_spanning_tree(self,printing=False):
        #Kruskals algo
        if len(self.nodes) <= 1: return self
        tree = Graph(self.nodes)
        possible_sorted_edges = list(self.connections)
        possible_sorted_edges = sorted(possible_sorted_edges, key= lambda x: int(x.value))
        while len(possible_sorted_edges) > 0:
            edge = possible_sorted_edges[0]
            if self.should_be_in_ST(edge,tree):
                tree._add_connection(edge)
                if printing:
                    print(edge.begg+" - "+edge.to+": "+edge.value)
            possible_sorted_edges.pop(0)
        return tree

    def should_be_in_ST(self,edge,tree):
        #Kruskals algo
        pocKompPred = len(tree._components())
        tree._add_connection(edge)
        pocKompPo = len(tree._components())
        tree.remove_connection(edge)
        return (pocKompPred - pocKompPo) == 1

    @staticmethod
    def _present_in_components(node,components):
        for comp in components:
            if node in comp.nodes:
                return True
        return False

    def _components(self):
        comp = set()
        for node in self.nodes:
            if not self._present_in_components(node,comp):
                c = Graph(self.__reachable_nodes(node))
                self.copy_connections_to(c)

                comp.add(c)
        return comp


    def copy_connections_to(self,component):
        for connection in self.connections:
            if connection.begg in component.nodes and connection.to in component.nodes:
                component._add_connection(connection)

    def remove_connection(self,edge):
        self.connections.remove(edge)

    def get_num_of_unique_neigbors(self,nodes):
        neigbors = set()
        for node in nodes:
            neigbors.update(self.get_neighbors(node))
        neigbors = neigbors - nodes
        return len(neigbors)

    def get_three_node_combinations_without_repetition(self):
        combinations = {frozenset([a, b, c]) for a in self.nodes for b in self.nodes for c in self.nodes}
        threeNodeCombinations = []
        for combination in combinations:
            if len(combination) == 3:
                threeNodeCombinations.append(combination)
        return threeNodeCombinations

    def get_three_nodes_with_most_unique_neigbors(self):
        combinations = self.get_three_node_combinations_without_repetition()
        mostNeighbors = 0
        bestCombination = None
        for combination in combinations:
            if self.get_num_of_unique_neigbors(set(combination)) > mostNeighbors:
                bestCombination = combination
                mostNeighbors = self.get_num_of_unique_neigbors(set(combination))
        return bestCombination

    def nodes_as_str(self,nodes):
        retStr = ""
        retStr += ', '.join(str(node) for node in nodes)
        return retStr

    def print(self):
        print(self.nodes)
        print(self.connections)

    def print_nodes_with_size_of_leaving_edges(self):
        nodes = self.nodes
        nodes.sort(reverse=True,key=self.get_leaving_edges_size)
        for node in nodes:
            print(node + " (" + str(self.get_leaving_edges_size(node))+")")
