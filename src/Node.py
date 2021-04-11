class Node:
    def __init__(self, name: str, predecessor=None, distance=None):
        self.name = name
        self.distance = distance
        self.predecessor = predecessor

    def __str__(self):
        if self.distance is not None and self.predecessor is not None:
            return "Node: " + self.name + " predecessor: " + str(self.predecessor) + " distance: " + str(self.distance)
        else:
            return self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
