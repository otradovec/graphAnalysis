#!/usr/bin/env python3
import sys
input_lines = []
for line in sys.stdin:
    input_lines.append(line)

connections = []
for i in range(2,len(input_lines)):
    connection = input_lines[i].replace("\r","").replace("\n","")
    connections.append(connection)

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
