class Connection:
    def __init__(self,begg,to,oriented: bool,value=1):
        self.begg = begg
        self.to = to
        self.oriented = oriented
        self.value = value
    def __str__(self):
        return "Connection: "+self.begg+" "+self.to+" "+str(self.oriented)+" "+str(self.value)
    def __repr__(self):
        return self.__str__()
    #def __eq__(self, other):
        #if not isinstance(other, Connection):
        #    return NotImplemented
        #return (self.begg == other.begg) and (self.to == other.to) and (self.oriented == other.oriented) and (self.value == other.value)
