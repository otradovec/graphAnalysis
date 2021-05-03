#!/usr/bin/env python3
import sys
input_lines = [line for line in sys.stdin]

connections = []
for line in input_lines:
    divided = "".join(line.split()).split(":")
    sourceNode = divided[0]
    destinationNodes = divided[1].split(",")
    for node in destinationNodes:
        node, value = node.split("(")
        value = value.replace(')', '')
        connections.append([sourceNode, node, value])
for conn in connections:
    if "+" in conn[0]:
        conn[0] = conn[0].replace('+', '')
        conn[2] = int(conn[2]) + int(1)
connections = [conn for conn in connections if conn[0] != conn[1]]
from src.Graph import Graph
g = Graph(set([row[0] for row in connections]).union(set([row[1] for row in connections])))
g.add_not_oriented_valued_connections(connections)
start_node = g.get_node(connections[0][0])
end_node = g.get_node(connections[-1][0])
g.invert_connection_values()

nodes_to_print = g.get_shortest_path_nodes(start_node, end_node)
distance = None
for node in nodes_to_print:
    if node == end_node:
        distance = - int(end_node.distance)

result = ""
for node in nodes_to_print:
    if result == "":
        result = result + node.name
    else:
        result = result + " -> " + node.name
result = result + ": " + str(int(distance))
print(result)
