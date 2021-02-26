class Graph:

    def __init__(self,nodes):
        self.nodes = nodes
        self.connections = []

    def has_node(self,nodeName):
        return nodeName in self.nodes

    def add_not_oriented_connection(self,first_node, second_node):
        if not self.has_node(first_node) or not self.has_node(second_node):
            raise ValueError("Adding connection with not  existing node")
        self.connections.append([first_node,second_node])
        self.connections.append([second_node,first_node])

    def add_not_oriented_connections(self,connections):
        for connection in connections:
            if len(connection) > 2:
                raise ValueError("Adding connection with too many arguments")
            self.add_not_oriented_connection(connection[0],connection[1])

    def is_connection(self,from_node, to_node):
        return [from_node,to_node] in self.connections

    def get_leaving_edges_size(self,node):
        leaving_edges_size = 0
        for connection in self.connections:
            if connection[0] == node:
                leaving_edges_size += 1
        return leaving_edges_size

    def print(self):
        print(self.nodes)
        print(self.connections)

    def print_nodes_with_size_of_leaving_edges(self):
        nodes = self.nodes
        nodes.sort(reverse=True,key=self.get_leaving_edges_size)
        for node in nodes:
            print(node + " (" + str(self.get_leaving_edges_size(node))+")")
