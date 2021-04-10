try:
    from Node import Node
except Exception as ignore:
    import src.Node
try:
    from .Node import Node
except Exception as e:
    pass
class Connection:
    def __init__(self, begg, to, oriented: bool, value=1):
        if type(begg) == Node:
            self.begg = begg
        else:
            self.begg = Node(begg)
        if type(to) == Node:
            self.to = to
        else:
            self.to = Node(to)
        self.oriented = oriented
        self.value = value

    def __str__(self):
        return "Connection: " + str(self.begg) + " " + str(self.to) + " " + str(self.oriented) + " " + str(self.value)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Connection):
            return NotImplemented
        return (self.begg == other.begg) and (self.to == other.to) and (self.oriented == other.oriented) and (
                    self.value == other.value)
