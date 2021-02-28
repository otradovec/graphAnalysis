import sys
input_lines = []
for line in sys.stdin:
    input_lines.append(line)

#first_stores = input_lines[0]
#first_stores = "".join(first_stores.split()).split(",")
#for i in range(0,len(first_stores)):
#    first_stores[i] = first_stores[i].lower()
#second_stores = input_lines[1]
#second_stores = "".join(second_stores.split()).split(",")
#from Graph import Graph
#g = Graph(set(first_stores) | set(second_stores))

connections = []
for i in range(2,len(input_lines)):
    connection = input_lines[i].replace("\r","").replace("\n","")#.lower()
#    connection = "".join(connection.split()).split("->")
    connections.append(connection)
#g.add_oriented_connections(connections)

simpleConnections = []
redundantConnections = []
for connection in connections:
    if connection.upper() in simpleConnections or connection.lower() in simpleConnections:
        redundantConnections.append(connection)
    else:
        simpleConnections.append(connection)
for simpleConnection in simpleConnections:
    print(simpleConnection)
print("----")
for redundantConnection in redundantConnections:
    print(redundantConnection)
