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
    def is_connection(self,from_node, to_node):
        return [from_node,to_node] in self.connections
