#!/usr/bin/env python3
import sys
input_lines = [line for line in sys.stdin]

connections = []
for line in input_lines:
    divided = "".join(line.split()).split(":")
    value = divided[1]
    nodes = divided[0].split("-")
    connections.append([nodes[0],nodes[1],value])
from src.Graph import Graph
g = Graph(set([row[0] for row in connections]).union(set([row[1] for row in connections])))
g.add_not_oriented_valued_connections(connections)
h = g.get_minimal_spanning_tree(printing=True)
print("Hodnoceni: " +  str(h.total_cost()))
