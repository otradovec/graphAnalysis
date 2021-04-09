#!/usr/bin/env python3
import sys
input_lines = [line for line in sys.stdin]

from src.Graph import Graph
g = Graph(set())
numbers = []
for line in input_lines:
    divided = "".join(line.split())
    numbers.append(divided)
#g.build_avl_tree(numbers)
#g.search_avl_wide(printing=True)
