#!/usr/bin/env python3
import sys
input_lines = [line for line in sys.stdin]

connections = []
for line in input_lines:
    divided = "".join(line.split()).split(":")
    value = divided[1]
    nodes = divided[0].split("-")
    connections.append([nodes[0], nodes[1], value])
from src.Graph import Graph

g = Graph(set([row[0] for row in connections]).union(set([row[1] for row in connections])))
g.add_not_oriented_valued_connections(connections)
nodes = list(g.get_dijkstra_valuated_nodes_from("Vy"))

def sorting_func(node):
    return node.distance


nodes.sort(key=sorting_func)
for node in nodes:
    print(node.name + ": " + str(int(node.distance)))
