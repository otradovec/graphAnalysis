class Graph:

    def __init__(self,nodes):
        self.nodes = nodes
    def hasNode(self,nodeName):
        return nodeName in self.nodes
