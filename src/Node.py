class Node:
    def __init__(self, name, predecessor=None, distance=None):
        self.name = name
        self.distance = distance
        self.predecessor = predecessor

    def __str__(self):
        if self.distance is not None and self.predecessor is not None:
            return "Node: " + self.name + " " + self.predecessor + " " + str(self.distance)
        else:
            return "Node: " + self.name

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return str(self) == str(other)
