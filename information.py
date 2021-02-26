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
    connection = "".join(connection.split()).split("-")
    connections.append(connection)
g.add_not_oriented_connections(connections)

print("Task 1:")
g.print_nodes_with_size_of_leaving_edges()
print()
