print("Hello world")
import sys
input_lines = []
for line in sys.stdin:
    input_lines.append(line)

names = input_lines[0]
names = "".join(names.split()).split(",")

connections = []
for i in range(1,len(input_lines)-1):
    print(input_lines[i])
    connection = input_lines[i]
    connection = "".join(connection.split()).split("-")
    connections.append(connection)
print(connections)
