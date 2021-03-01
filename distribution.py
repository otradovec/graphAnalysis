import sys
input_lines = []
for line in sys.stdin:
    input_lines.append(line)

names = input_lines[0]
names = "".join(names.split()).split(",")
from Graph import Graph
g = Graph(names)

connections = []
for i in range(1,len(input_lines)):
    connection = input_lines[i]
    connectionValue = "".join(connection.split()).split(":")[0]
    connectionLine = "".join(connection.split()).split(":")[1].split(">")
    for i in range(1,len(connectionLine)):
        connections.append([connectionLine[i-1],connectionLine[i],connectionValue])

g.add_oriented_connections(connections)
g.print()
topNode = g.get_node_with_highest_degree()
print("nejvice navstevovany: " +  topNode + " " + str(g.get_degree(topNode)))
#print("existuje vice spojeni mezi dvema mesty: " + )
