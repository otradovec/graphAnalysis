import sys
input_lines = []
for line in sys.stdin:
    input_lines.append(line)

names = input_lines[0]
names = "".join(names.split()).split(",")
from Graph import Graph
g = Graph(names)

connections = []
edge_value_touching_all_nodes = None
for i in range(1,len(input_lines)):
    connection = input_lines[i]
    connectionValue = "".join(connection.split()).split(":")[0]
    connectionLine = "".join(connection.split()).split(":")[1].split(">")
    if set(connectionLine) == set(names):
        edge_value_touching_all_nodes = connectionValue
    for i in range(1,len(connectionLine)):
        connections.append([connectionLine[i-1],connectionLine[i],connectionValue])
def anoNe(boolean):
    return "ano" if boolean else "ne"

def ne_if_none(object):
    return object if object else "ne"

g.add_oriented_connections(connections)
topNode = g.get_node_with_highest_degree()
print("nejvice navstevovany: " +  topNode + " " + str(g.get_degree(topNode)))
print("existuje vice spojeni mezi dvema mesty: " + anoNe(g.is_multigraph()))
print("nesmyslna smycka: " + anoNe(g.has_loop()))
print("mesto bez zasobeni: " + anoNe(g.has_connectivity()))
print("vsechna prima spojeni: "  + anoNe(g.is_complete()))
print("obousmerne trasy: " + anoNe(g.is_bidirectional()))
print("rovnovaha v dopravni siti: " + anoNe(g.all_nodes_have_equal_in_out_degree()))
print("navstivil nekdo vsechna mesta: " + ne_if_none(edge_value_touching_all_nodes))
